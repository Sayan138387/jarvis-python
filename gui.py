import tkinter as tk
import threading

from listen import take_command
from actions import execute_command
from speech import speak


# =========================
# Main Window
# =========================

root = tk.Tk()

root.title("JARVIS")
root.geometry("900x650")
root.configure(bg="#0a0a0a")


# =========================
# Functions
# =========================

def start_listening():

    status_label.config(text="Status: Listening...")

    chat_box.insert(tk.END, "\n🎤 Listening...\n")
    chat_box.see(tk.END)

    command = take_command()

    if command:

        chat_box.insert(tk.END, f"\n👤 You: {command}\n")

        response = execute_command(command)

        if response:

            chat_box.insert(
                tk.END,
                f"🤖 Jarvis: {response}\n"
            )

            speak(response)

        else:

            chat_box.insert(
                tk.END,
                "🤖 Jarvis: I don't understand that command.\n"
            )

            speak("I don't understand that command.")

    else:

        chat_box.insert(
            tk.END,
            "\n🤖 Jarvis: Sorry, I could not understand.\n"
        )

    chat_box.see(tk.END)

    status_label.config(text="Status: Ready")


def start_thread():

    threading.Thread(
        target=start_listening,
        daemon=True
    ).start()


# =========================
# Title
# =========================

title = tk.Label(
    root,
    text="J.A.R.V.I.S",
    font=("Consolas", 30, "bold"),
    fg="#00ffff",
    bg="#0a0a0a"
)

title.pack(pady=15)


# =========================
# Status Label
# =========================

status_label = tk.Label(
    root,
    text="Status: Ready",
    font=("Consolas", 14),
    fg="#00ff99",
    bg="#0a0a0a"
)

status_label.pack(pady=5)


# =========================
# Chat Box Frame
# =========================

frame = tk.Frame(root)

frame.pack(pady=15)


# =========================
# Scrollbar
# =========================

scrollbar = tk.Scrollbar(frame)

scrollbar.pack(
    side=tk.RIGHT,
    fill=tk.Y
)


# =========================
# Chat Box
# =========================

chat_box = tk.Text(
    frame,
    height=22,
    width=85,
    font=("Consolas", 12),
    bg="#111111",
    fg="#00ffff",
    insertbackground="#00ffff",
    yscrollcommand=scrollbar.set
)

chat_box.pack(
    side=tk.LEFT
)

scrollbar.config(
    command=chat_box.yview
)


# =========================
# Startup Message
# =========================

chat_box.insert(
    tk.END,
    """
========================================
        J.A.R.V.I.S ONLINE
========================================

🤖 Jarvis: Systems initialized.

"""
)


# =========================
# Activate Button
# =========================

button = tk.Button(
    root,
    text="🎤 ACTIVATE JARVIS",
    command=start_thread,
    font=("Consolas", 14, "bold"),
    bg="#00ffff",
    fg="black",
    padx=20,
    pady=10
)

button.pack(pady=20)


# =========================
# Run App
# =========================
root.after(
    1000,
    lambda: speak(
        "Hello Sayan. How can I help you today?"
    )
)
root.mainloop()