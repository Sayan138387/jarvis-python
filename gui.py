from listen import take_command
from actions import execute_command
from brain import process_command
from speech import speak
import tkinter as tk

root = tk.Tk()

root.title("JARVIS")
root.geometry("700x500")

title = tk.Label(
    root,
    text="JARVIS",
    font=("Arial", 24, "bold")
)

title.pack(pady=10)

chat_box = tk.Text(
    root,
    height=20,
    width=70
)

chat_box.pack(pady=10)

chat_box.insert(tk.END, "Jarvis: Ready.\n")

def start_listening():
    chat_box.insert(tk.END, "\nListening...\n")

def start_listening():

    chat_box.insert(tk.END, "\nListening...\n")
    chat_box.see(tk.END)

    command = take_command()

    if command == "":
        return

    chat_box.insert(tk.END, f"\nYou: {command}\n")

    action_response = execute_command(command)

    if action_response:

        chat_box.insert(
            tk.END,
            f"Jarvis: {action_response}\n"
        )

        speak(action_response)

    else:

        response = process_command(command)

        chat_box.insert(
            tk.END,
            f"Jarvis: {response}\n"
        )

        speak(response)

    chat_box.see(tk.END)
# BUTTON 
button = tk.Button(
    root,
    text="🎤 Start Listening",
    command=start_listening,
    font=("Arial", 12)
)

button.pack(pady=10)

root.mainloop()