def chatbot_response(user_input):
    if user_input.lower() == "hello":
        return "Hi!"
    elif user_input.lower() == "how are you":
        return "I'm fine, thanks!"
    elif user_input.lower() == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."

while True:
    user_input = input("Me : ")
    response = chatbot_response(user_input)
    print("Bot:", response)
    if user_input.lower() == "bye":
        break
