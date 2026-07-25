import os
from pathlib import Path

def show_menu():
    print("\n===================================")
    print("@@@@@@@@%%%***+------------==+#%@@@")
    print("@@@@@@@@##%*+++=-------------+**@@@")
    print("@@@@@@@@@*#*=++=-----------=+**#@@@")
    print("@@@@@@@@@%#***+=--------+++****@@@@")
    print("@@@@@@@@@@%**+=-------:---=+++*++@@")
    print("@@@@@@@@@@%+======--=--==-==+**%%@@")
    print("@@@@@@@@@@@@%%@@@%%*#*####+###*@#@@")
    print("@@@@@@@@@#@@@%*%@@#-*@@@@@@@#++=@@@")
    print("@@@@@@@@@%++**+===-:-=+++***+=+%@@@")
    print("@@@@@@@@@@#+=--=++-:-=--===+++*@@@@")
    print("@@@@@@@@@@@@+=++*=-:-==--=+*#+@@@@@")
    print("@@@@@@@@@@%%@#*##=--=--++=*##*@@@@@")
    print("@@@@@@@@@@%*%%*@@@@@@%===*+##%%@@@@")
    print("@@@@@#@@@@@%*%@%@@@@++*%*+*#===--@@")
    print("@@@---=@@@@@@#*@%*++**++**%@--=---#")
    print("@@-----@@@@@@@*++*---===*@@*------%")
    print("%------=@@@@@@@%*+=-=+#@@@**=+=--=%")
    print("--------%@@@@@@@@@@@@@@@@#**#=----%")
    print("--------%@@@@@@@@@@@@@@@@#**#=----%")
    print("Rushmore: Developer Command Assistant")
    print("===================================")
    print("1. Show current directory")
    print("2. Create project folder")
    print("3. Organise files")
    print("4. Count words in a text file")
    print("5. Exit")

def show_current_directory():
    current = Path.cwd()
    print(f"\nCurrent directory:\n{current}")

def create_project():
    project_name = input("Enter project name: ")

    project = Path(project_name)
    project.mkdir(exist_ok=True)

    (project / "src").mkdir(exist_ok=True)
    (project / "docs").mkdir(exist_ok=True)
    (project / "tests").mkdir(exist_ok=True)

    readme = project / "README.md"

    with open(readme, "w") as file:
        file.write(f"# {project_name}\n\n")
        file.write("Project created using Developer Command Assistant.\n")
    
    (project / ".gitignore").touch()

    print(f"\nProject '{project_name}' created successfully")

def main():
    while True:
        show_menu()

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_current_directory()

        elif choice == "2":
            create_project()    
        
        elif choice == "5":
            print("Rushmore Offline")
            break

        else:
            print("Feature coming soon.")


if __name__ == "__main__":
    main()
