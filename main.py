from pathlib import Path

from organizer import organize_folder
from duplicate import find_duplicates
from undo import undo_last_action


folder_path = input("Enter folder path: ").strip()
folder = Path(folder_path)


if not folder.exists() or not folder.is_dir():
    print("Invalid folder path.")

else:
    while True:
        print("\n===== FILE ORGANIZER =====")
        print("1. Organize Files")
        print("2. Find Duplicates")
        print("3. Undo Last Action")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()


        if choice == "1":
            organize_folder(folder_path)

            print("Files organized successfully!")


        elif choice == "2":
            duplicates = find_duplicates(folder_path)

            if duplicates:
                print("\nDuplicate files found:")

                for original, duplicate in duplicates:
                    print(f"\nOriginal:  {original}")
                    print(f"Duplicate: {duplicate}")

            else:
                print("No duplicate files found.")


        elif choice == "3":
            result = undo_last_action()
            print(result)


        elif choice == "4":
            print("Program closed.")
            break


        else:
            print("Invalid choice.")