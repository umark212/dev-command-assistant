from pathlib import Path

class TextManager:
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
