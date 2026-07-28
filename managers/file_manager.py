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
        
        self.logger.log(f"Organised files in {folder}")




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
            self.logger.log(f"Searched for '{filename}'")
        else:
            print("\nNo matching files found.")


    def folder_statistics(self):
        folder = input("Folder (leave blank for current directory): ").strip()

        if folder:
            root = Path(folder)
        else:
            root = Path.cwd()

        if not root.exists():
            print("Folder does not exist.")
            return

        if not root.is_dir():
            print("That is not a folder.")
            return

        total_files = 0  #create counters
        total_folders = 0
        total_size = 0
        largest_file = None
        largest_size = 0

        for item in root.rglob("*"):
            if item.is_file:
                total_files += 1
                size = item.stat().st_size #stat() gets metadata from os and st_size i got from path library to get size in bytes
                total_size += size  

                if size > largest_size:  #keeps track of maximum seen so far
                    largest_size = size
                    largest_file = item

            elif item.is_dir():
                total_folders += 1

            #get average
            if total_files > 0:
                average_size = total_size / total_files
            else:
                average_size = 0


        print("\n========== Folder Statistics ==========\n")
        print(f"Folder: {root}")
        print(f"\nFiles: {total_files}")
        print(f"Folders: {total_folders}")
        print(f"\nTotal Size: {self.format_size(total_size)}")
        print(f"Average File Size: {self.format_size(average_size)}")
        
        if largest_file:
            print(f"\nLargest File: {largest_file.name}")
            print(f"Largest Size: {self.format_size(largest_size)}")

        self.logger.log(f"Generated statistics for {root}")


                    
    def format_size(self, size):   #to convert the sizes metadata into readable format
        units = ["B", "KB", "MB", "GB", "TB"]

        for unit in units:
            if size < 1024:
                return f"{size:.2f} {unit}" #more formatting, & keep dividing by 1024 until small enough

            size /= 1024

        return f"{size:.2f} PB"
