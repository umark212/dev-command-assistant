#assistant, all functions to be added here.

from pathlib import Path
import os
import shutil


class DeveloperAssistant:

    def show_current_directory(self):
        current = Path.cwd()
        print(f"\nCurrent directory:\n{current}")

    def create_project(self):
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

    def organise_files(self):
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


    def count_words(self):

        file_path = input("Enter the path to a text file: ")

        try:   #we use try so we dont crash if file not found
            with open(file_path, "r", encoding="utf-8") as file:

                text = file.read()

            words = text.split() #split automatically separates on whitespace

            characters = len(text) #returns number of characters, spaces etc.

            lines = text.count("\n") + 1 #eg. if theres 2 separators that means theres 3 lines, so +1 

            print("\n===== Text Analysis =====")
            print(f"Words: {len(words)}")
            print(f"Characters: {characters}")
            print(f"Lines: {lines}")

        except FileNotFoundError:
            print("File not found.")      #print these messages instead

        except Exception as e:
            print(f"An error occurred: {e}")

