from pathlib import Path
import shutil #moves the files

class FileManager:
    def show_current_directory(self):
        current = Path.cwd()
        print(f"\nCurrent directory:\n{current}")

    

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





    def search_file(self):

        filename = input("Enter filename to search for: ").strip() #strip useful for searching because removes whitespaces
        
        start = input("Folder to search (leave blank for current directory): ").strip()

        if start:
            root = Path(start)
        else:
            root = Path.cwd()


        if not root.exists():
            print("Folder does not exist.")
            return

        matches = []

        for file in root.rglob("*"): #rgblob useful pathlib feature, lets us recursively walk each folder, all files (*)
            if file.is_file():
                if filename.lower() in file.name.lower(): #case insensitive searching: searches regardless of capitilization
                    matches.append(file)  #appends to list we created
                    
        if matches:
            print(f"\nFound {len(matches)} matches:\n")
            for match in matches:
                print(match)
        else:
            print("\nNo matching files found.")
