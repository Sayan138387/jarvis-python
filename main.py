from speech import speak
from brain import process_command
from listen import take_command
from actions import execute_command

speak("Hello Sayan. I am Jarvis.")

while True:

    command = take_command()

    if command == "":
        continue

    action_response = execute_command(command)

    if action_response:
        print("Jarvis:", action_response)
        speak(action_response)

    else:
        response = process_command(command)

        print("Jarvis:", response)
        speak(response)

    if "bye" in command:
        break