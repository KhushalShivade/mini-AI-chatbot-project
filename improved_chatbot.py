from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load DialoGPT-medium
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

print("🤖 Hello! I’m your AI chatbot. Type 'bye' to quit.")

# Start empty chat history
chat_history_ids = None

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Bot: Goodbye! 👋")
        break

    # Encode user input with end-of-sentence token
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

    # Append conversation to history
    if chat_history_ids is not None:
        bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1)
    else:
        bot_input_ids = new_input_ids

    # Generate response
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,          # randomness
        top_k=50,                # top 50 choices
        top_p=0.95,              # nucleus sampling
        temperature=0.7          # creativity
    )

    # Decode only the new tokens
    bot_response = tokenizer.decode(
        chat_history_ids[:, bot_input_ids.shape[-1]:][0],
        skip_special_tokens=True
    )

    print(f"Bot: {bot_response}")
