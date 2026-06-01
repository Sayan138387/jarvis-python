import webbrowser
import datetime

def execute_command(command):

    if "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "what time is it" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The time is {current_time}"

    elif "open github" in command:
        webbrowser.open("https://github.com")
        return "Opening GitHub"

    elif "open chatgpt" in command:
        webbrowser.open("https://chatgpt.com")
        return "Opening ChatGPT"

    elif "open gmail" in command:
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail"

    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
        return "Opening LinkedIn"

    return None