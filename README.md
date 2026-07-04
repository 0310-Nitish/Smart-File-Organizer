# 📁 Smart File Organizer

A Python-based file organization automation tool that automatically sorts files into folders based on their file extensions. The application also supports duplicate file detection, custom organization rules, undo functionality, activity logging, and both CLI and GUI interfaces.

## ✨ Features

- Automatically organize files by extension
- Detect duplicate files using SHA-256 hashing
- Ignore empty files during duplicate scanning
- Configure custom folder rules using JSON
- Undo the last file movement
- Maintain an activity log of organized files
- Prevent filename conflicts using automatic renaming
- Simple command-line interface
- User-friendly Tkinter GUI

## 🛠️ Tech Stack

- Python
- Tkinter
- pathlib
- shutil
- hashlib
- JSON
- datetime

No external Python packages are required.

## 📂 Project Structure

```text
File-Organizer/
│
├── main.py              # CLI interface
├── gui.py               # Tkinter GUI interface
├── organizer.py         # File organization logic
├── duplicate.py         # Duplicate detection
├── undo.py              # Undo and history management
├── logger.py            # Activity logging
├── config.json          # Custom organization rules
│
├── requirements.txt
├── .gitignore
└── README.md