from pathlib import Path
import shutil
import json

from logger import log_action
from undo import save_history


BASE_DIR = Path(__file__).resolve().parent
CONFIG_FILE = BASE_DIR / "config.json"


def load_rules():
    with open(CONFIG_FILE, "r") as file:
        rules = json.load(file)

    return rules


def get_unique_destination(destination):
    if not destination.exists():
        return destination

    parent = destination.parent
    stem = destination.stem
    suffix = destination.suffix

    counter = 1

    while True:
        new_destination = parent / f"{stem}_{counter}{suffix}"

        if not new_destination.exists():
            return new_destination

        counter += 1


def organize_folder(folder_path):
    folder = Path(folder_path)
    rules = load_rules()

    for item in folder.iterdir():

        # Ignore folders
        if not item.is_file():
            continue

        extension = item.suffix.lower()

        if extension in rules:
            folder_name = rules[extension]

            destination_folder = folder / folder_name
            destination_folder.mkdir(exist_ok=True)

            destination = destination_folder / item.name
            destination = get_unique_destination(destination)

            shutil.move(str(item), str(destination))

            save_history(item, destination)

            log_action(
                f"MOVED | {item.name} -> "
                f"{folder_name}/{destination.name}"
            )

            print(
                f"Moved: {item.name} -> "
                f"{folder_name}/{destination.name}"
            )