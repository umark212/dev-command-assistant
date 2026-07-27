import os
import time

from ascii_art import MAIN_FACE, FACE_1, FACE_2, FACE_3, FACE_4


class AsciiAnimator:

    def __init__(self):

        self.main = MAIN_FACE

        self.animation = [
            FACE_1,
            FACE_2,
            FACE_3
            FACE_4
        ]

        self.counter = 0

    def clear(self):

        os.system("cls" if os.name == "nt" else "clear") #os library way to clear


 
