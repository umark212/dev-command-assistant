import os
import time

from ascii_art import MAIN_FACE, FACE_1, FACE_2, FACE_3, FACE_4


class AsciiAnimator:

    def __init__(self):

        self.faces = [
            MAIN_FACE,
            FACE_1,
            FACE_2,
            FACE_3,
            FACE_4
        ]

        self.counter = 0

    def clear(self):
        #os library way to clear windows terminal with cls or clear
        os.system("cls" if os.name == "nt" else "clear") 


 
    def display(self):

        self.clear()
        #select different face each time menu displays
        current_face = self.faces[self.counter % len(self.faces)] #using list and counter created earlier to increment through it

        print(current_face)
        
        self.counter += 1

