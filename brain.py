def process_command(command):

    command = command.lower()

    if "hello" in command:
        return "Hello Sayan. How can I help you?"

    elif "who are you" in command:
        return "I am Jarvis, your personal voice assistant."

    elif "how are you" in command:
        return "I am doing great. Thanks for asking."

    elif "what is your name" in command:
        return "My name is Jarvis."

    elif "good morning" in command:
        return "Good morning Sayan. Have a productive day."

    elif "good afternoon" in command:
        return "Good afternoon Sayan."

    elif "good evening" in command:
        return "Good evening Sayan."

    elif "thank you" in command:
        return "You are welcome."

    elif "bye" in command:
        return "Goodbye Sayan. Have a great day."

    else:
        return "I don't understand that command."