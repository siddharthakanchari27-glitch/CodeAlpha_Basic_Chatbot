# CodeAlpha Task 4: Basic Chatbot

def chatbot():
    print("===== Welcome to Basic Chatbot =====")
    print("Type 'hello', 'how are you', or 'bye'.")

    while True:
        user_input = input("\nYou: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hi!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

    print("Chat ended. Thank you!")


# Start the chatbot
chatbot()
