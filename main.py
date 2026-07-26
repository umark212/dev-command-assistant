import shutil   #python library for moving and copying files
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

def organise_files():
    folder = input("Enter folder path: ")
    folder = Path(folder)

    if not folder.exists():
        print("Folder not found.")
        return

    categories = {           #dictionary use
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",    #eg. if file png put in images folder

        ".pdf": "Documents",
        ".txt": "Documents",
        ".docx": "Documents",

        ".mp3": "Audio",

        ".mp4": "Videos"
    }

    for file in folder.iterdir():     #look at everything inside folder

        if file.is_file():            #only files not other folders

            extension = file.suffix.lower()  #eg. PDF = .pdf to match dictionary

            if extension in categories:

                destination = folder / categories[extension]  # / means it joins new folder and eg. categories[.jpg] = images from dictionary, to create images folder

                destination.mkdir(exist_ok=True)   #mkdir is make directory if it doesnt already exist

                shutil.move(str(file), str(destination / file.name))  #move file into the folder, using str so shutil.move accepts it always

    print("Files organised successfully!")

def main():
    while True:
        show_menu()

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_current_directory()

        elif choice == "2":
            create_project()

        elif choice == "3":
            organise_files()
        
        elif choice == "5":
            print("Rushmore Offline")
            break

        else:
            print("Feature coming soon.")


if __name__ == "__main__":
    main()
