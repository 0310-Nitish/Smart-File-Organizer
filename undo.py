import json
import shutil
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
HISTORY_FILE = BASE_DIR / "history.json"


def save_history(original_path, destination_path):
    history = []

    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r") as file:
            history = json.load(file)

    history.append({
        "original": str(original_path),
        "destination": str(destination_path)
    })

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def undo_last_action():
    if not HISTORY_FILE.exists():
        return "No action to undo."

    with open(HISTORY_FILE, "r") as file:
        history = json.load(file)

    if not history:
        return "No action to undo."

    last_action = history[-1]

    original = Path(last_action["original"])
    destination = Path(last_action["destination"])

    if not destination.exists():
        return "File could not be restored because it was not found."

    shutil.move(
        str(destination),
        str(original)
    )

    history.pop()

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)

    return f"Restored: {destination.name}"