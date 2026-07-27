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
    print("5. Exit")



while True:
    show_menu()

    choice = input("\nChoose an option: ")

    if choice == "1":
        assistant.show_current_directory()

    elif choice == "2":
        assistant.create_project()

    elif choice == "3":
        assistant.organise_files()

    elif choice == "4":
        assistant.count_words()
                                        
    elif choice == "5":
        print("Rushmore Offline")
        break

    else:
        print("Invalid Option")


