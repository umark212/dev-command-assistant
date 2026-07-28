from assistant import DeveloperAssistant
from animator import AsciiAnimator

assistant = DeveloperAssistant()
animator = AsciiAnimator()


def show_menu():
    print("\n===================================")
    animator.display()
    print("Rushmore: Developer Command Assistant")
    print("===================================")
    print("1. Show current directory")
    print("2. Create project folder")
    print("3. Organise files")
    print("4. Count words in a text file")
    print("5. Search for file")
    print("6. Folder Statistics")
    print("7. View activity log")
    print("8. Exit")



while True:
    show_menu()

    choice = input("\nChoose an option: ")

    if choice == "1":
        assistant.files.show_current_directory()

    elif choice == "2":
        assistant.projects.create_project()

    elif choice == "3":
        assistant.files.organise_files()

    elif choice == "4":
        assistant.text.count_words()
                                        
    elif choice == "5":
        assistant.files.search_file()

    elif choice == "6":
        assistant.files.folder_statistics()

    elif choice == "7":
        assistant.logger.view_log()

    elif choice == "8":
        print("Rushmore Offline")
        break
    
    else:
        print("Invalid Option")


