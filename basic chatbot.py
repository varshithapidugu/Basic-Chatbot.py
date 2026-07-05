# Function to generate chatbot responses
def chatbot(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what is your name":
        return "I am a simple chatbot."
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."

print("=== Simple Rule-Based Chatbot ===")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ")
    reply = chatbot(user)
    print("Bot:", reply)

    if user.lower() == "bye":
        break