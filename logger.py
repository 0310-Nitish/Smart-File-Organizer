from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "activity.log"


def log_action(message):
    current_time = datetime.now()

    formatted_time = current_time.strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(
            f"{formatted_time} | {message}\n"
        )