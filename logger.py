from datetime import datetime


def log_action(message):

    current_time = datetime.now()

    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    with open("activity.log", "a") as file:
        file.write(f"{formatted_time} | {message}\n")