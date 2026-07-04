import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

from organizer import organize_folder
from duplicate import find_duplicates
from undo import undo_last_action


selected_folder = ""


def show_output(message):
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, message)


def select_folder():
    global selected_folder

    folder = filedialog.askdirectory()

    if folder:
        selected_folder = folder
        folder_label.config(text=folder)
        status_label.config(text="Folder selected successfully")
        show_output("Selected folder:\n" + folder)


def organize_files():
    if not selected_folder:
        messagebox.showwarning(
            "Warning",
            "Please select a folder first."
        )
        return

    try:
        organize_folder(selected_folder)

        status_label.config(
            text="Files organized successfully"
        )

        show_output(
            "Files organized successfully!\n\n"
            "Check the selected folder to see organized files."
        )

    except Exception as error:
        messagebox.showerror(
            "Error",
            str(error)
        )


def check_duplicates():
    if not selected_folder:
        messagebox.showwarning(
            "Warning",
            "Please select a folder first."
        )
        return

    try:
        duplicates = find_duplicates(selected_folder)

        if duplicates:
            result = "DUPLICATE FILES FOUND\n"
            result += "=" * 50 + "\n\n"

            for duplicate, original in duplicates:
                result += f"Original:\n{original}\n\n"
                result += f"Duplicate:\n{duplicate}\n"
                result += "-" * 50 + "\n\n"

            show_output(result)

            status_label.config(
                text=f"{len(duplicates)} duplicate(s) found"
            )

        else:
            show_output("No duplicate files found.")
            status_label.config(
                text="Duplicate scan completed"
            )

    except Exception as error:
        messagebox.showerror(
            "Error",
            str(error)
        )


def undo_action():

    try:
        result = undo_last_action()

        status_label.config(
            text=result
        )

        show_output(result)

    except Exception as error:

        messagebox.showerror(
            "Error",
            str(error)
        )

def view_log():
    log_file = Path("activity.log")

    if not log_file.exists():
        show_output("No activity log found yet.")
        return

    with open(log_file, "r") as file:
        logs = file.read()

    if logs:
        show_output(logs)
    else:
        show_output("Activity log is empty.")

    status_label.config(
        text="Activity log loaded"
    )


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()

root.title("Smart File Organizer")
root.geometry("850x650")
root.resizable(False, False)


# ---------------- TITLE ----------------

title_label = tk.Label(
    root,
    text="Smart File Organizer",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=20)


subtitle_label = tk.Label(
    root,
    text="Organize, detect duplicates and restore files easily",
    font=("Arial", 11)
)

subtitle_label.pack(pady=5)


# ---------------- FOLDER SECTION ----------------

select_button = tk.Button(
    root,
    text="Select Folder",
    width=22,
    height=2,
    command=select_folder
)

select_button.pack(pady=10)


folder_label = tk.Label(
    root,
    text="No folder selected",
    wraplength=750
)

folder_label.pack(pady=5)


# ---------------- ACTION BUTTONS ----------------

button_frame = tk.Frame(root)
button_frame.pack(pady=15)


organize_button = tk.Button(
    button_frame,
    text="Organize Files",
    width=18,
    height=2,
    command=organize_files
)

organize_button.grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)


duplicate_button = tk.Button(
    button_frame,
    text="Find Duplicates",
    width=18,
    height=2,
    command=check_duplicates
)

duplicate_button.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)


undo_button = tk.Button(
    button_frame,
    text="Undo Last Action",
    width=18,
    height=2,
    command=undo_action
)

undo_button.grid(
    row=0,
    column=2,
    padx=5,
    pady=5
)


log_button = tk.Button(
    button_frame,
    text="View Activity Log",
    width=18,
    height=2,
    command=view_log
)

log_button.grid(
    row=0,
    column=3,
    padx=5,
    pady=5
)


# ---------------- OUTPUT AREA ----------------

output_label = tk.Label(
    root,
    text="Output",
    font=("Arial", 12, "bold")
)

output_label.pack()


output_text = tk.Text(
    root,
    height=15,
    width=95,
    wrap=tk.WORD
)

output_text.pack(
    padx=20,
    pady=10
)


# ---------------- STATUS BAR ----------------

status_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 10),
    relief=tk.SUNKEN,
    anchor="w"
)

status_label.pack(
    side=tk.BOTTOM,
    fill=tk.X
)


root.mainloop()