import webbrowser
import datetime
import urllib.parse

from weather import get_weather

def execute_command(command):

    command = command.lower()

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

    elif "weather in" in command:

        city = command.replace("weather in", "").strip()

        return get_weather(city)

    elif "search" in command:

        query = command.replace("search", "").strip()

        if query:

            url = "https://www.google.com/search?q=" + urllib.parse.quote(query)

            webbrowser.open(url)

            return f"Searching {query}"

        else:
            return "Please tell me what to search."

    return None