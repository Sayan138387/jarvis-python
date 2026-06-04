import os
import webbrowser
import datetime
import urllib.parse

from weather import get_weather
from fun import get_joke, get_quote, get_fact
from notes import create_note

def execute_command(command):

    command = command.lower()

    # =========================
    # Websites
    # =========================

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

    elif "open spotify" in command or "play music" in command:
        webbrowser.open("https://open.spotify.com")
        return "Opening Spotify"

    # =========================
    # Desktop Applications
    # =========================

    elif "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad"

    elif "open calculator" in command:
        os.system("calc")
        return "Opening Calculator"

    elif "open command prompt" in command:
        os.system("start cmd")
        return "Opening Command Prompt"

    elif "open vscode" in command:
        os.system("code")
        return "Opening Visual Studio Code"

    # =========================
    # Folders
    # =========================

    elif "open downloads" in command:
        return "Downloads folder support will be improved soon."

    elif "open documents" in command:
        return "Documents folder support will be improved soon."

    # =========================
    # Time
    # =========================

    elif "what time is it" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The time is {current_time}"

    # =========================
    # Weather
    # =========================

    elif "weather in" in command:

        city = command.replace("weather in", "").strip()

        return get_weather(city)

    # =========================
    # Google Search
    # =========================

    elif "search" in command:

        query = command.replace("search", "").strip()

        if query:

            url = (
                "https://www.google.com/search?q="
                + urllib.parse.quote(query)
            )

            webbrowser.open(url)

            return f"Searching {query}"

        else:
            return "Please tell me what to search."

    # =========================
    # Notes
    # =========================

    elif command.startswith("note"):

        note_text = command.replace("note", "").strip()

        if note_text:
            return create_note(note_text)

        return "Please tell me what to write."

    # =========================
    # Fun Commands
    # =========================

    elif "tell me a joke" in command or "joke" in command:
        return get_joke()

    elif "tell me a quote" in command or "quote" in command:
        return get_quote()

    elif "tell me a fact" in command or "fact" in command:
        return get_fact()

    return None