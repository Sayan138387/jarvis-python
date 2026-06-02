import webbrowser
import datetime
import urllib.parse

def execute_command(command):

    if "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google"

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

    elif "what time is it" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The time is {current_time}"

    elif "search" in command:

        query = command.replace("search", "").strip()

        if query:

            url = "https://www.google.com/search?q=" + urllib.parse.quote(query)

            webbrowser.open(url)

            return f"Searching {query}"

    return None