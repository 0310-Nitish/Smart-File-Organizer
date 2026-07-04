import hashlib
from pathlib import Path


def calculate_hash(file_path):
    hasher = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()


def find_duplicates(folder_path):
    folder = Path(folder_path)

    hashes = {}
    duplicates = []

    for file in folder.rglob("*"):

        if not file.is_file():
            continue

        # Skip empty files
        if file.stat().st_size == 0:
            continue

        file_hash = calculate_hash(file)

        if file_hash in hashes:
            original = hashes[file_hash]
            duplicates.append((original, file))
        else:
            hashes[file_hash] = file

    return duplicates