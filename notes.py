from datetime import datetime

def create_note(note_text):

    now = datetime.now()

    filename = f"note_{now.strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as file:
        file.write(note_text)

    return f"Note saved as {filename}"