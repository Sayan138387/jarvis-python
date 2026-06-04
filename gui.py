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

button = tk.Button(
    root,
    text="Start Listening",
    command=start_listening
)

button.pack(pady=10)

root.mainloop()