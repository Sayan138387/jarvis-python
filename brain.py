def process_command(command):

    command = command.lower()

    if "hello" in command:
        return "Hello Sayan."

    elif "how are you" in command:
        return "I am fine."

    elif "bye" in command:
        return "Goodbye."

    elif "who created you" in command:
        return "Sayan Created me."

    elif "who are you" in command:
        return "I am Jarvis, your personal assistant."

    elif "good morning" in command:
        return "Good morning Sayan. Have a productive day."

    elif "thank you" in command:
        return "You are welcome."

    elif "what is your name" in command:
        return "My name is Jarvis."

    elif "how old are you" in command:
        return "I was created recently, so I am very young."
        
    else:
        return "Sorry, I do not understand."