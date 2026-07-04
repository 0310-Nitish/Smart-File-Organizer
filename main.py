from organizer import organize_folder
from duplicate import find_duplicates
from undo import undo_last_action


folder_path = input("Enter folder path: ")


while True:

    print("\n===== FILE ORGANIZER =====")
    print("1. Organize Files")
    print("2. Find Duplicates")
    print("3. Undo Last Action")
    print("4. Exit")   

    

    choice = input("Enter your choice: ")


    if choice == "1":

        organize_folder(folder_path)

        print("Files organized successfully!")


    elif choice == "2":

        duplicates = find_duplicates(folder_path)

        if duplicates:

            print("\nDuplicate files found:")

            for duplicate, original in duplicates:
                print(f"\nOriginal:  {original}")
                print(f"Duplicate: {duplicate}")

        else:
            print("No duplicate files found.")


            
    elif choice == "3":
        undo_last_action()      


    elif choice == "4":

        print("Program closed.")
        break


    else:
        print("Invalid choice.")