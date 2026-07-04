import json
import shutil
from pathlib import Path

HISTORY_FILE = "history.json"


def save_history(original_path, destination_path):

    history = []

    if Path(HISTORY_FILE).exists():
        with open(HISTORY_FILE, "r") as file:
            history = json.load(file)

    history.append({
        "original": str(original_path),
        "destination": str(destination_path)
    })

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)

def undo_last_action():

    if not Path(HISTORY_FILE).exists():
        return "No action to undo."

    with open(HISTORY_FILE, "r") as file:
        history = json.load(file)

    if not history:
        return "No action to undo."

    last_action = history.pop()

    original = Path(last_action["original"])
    destination = Path(last_action["destination"])

    if destination.exists():

        shutil.move(
            str(destination),
            str(original)
        )

        message = f"Restored: {destination.name}"

    else:
        message = "File could not be restored because it was not found."

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)

    return message