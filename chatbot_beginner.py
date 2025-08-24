# chatbot.py
def chatbot():
    print("🤖 Hello! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user = input("You: ").lower()
        if user == "bye":
            print("Bot: Goodbye! 👋")
            break
        elif "hello" in user:
            print("Bot: Hi there! How can I help?")
        elif "name" in user:
            print("Bot: I'm a chatbot made in Python!")
        else:
            print("Bot: Sorry, I don't understand that yet.")

chatbot()
