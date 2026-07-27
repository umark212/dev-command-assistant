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


 
    def display(self):

        self.counter += 1

        #play animation every 10 menu displays
        if self.counter % 10 == 0:
            for frame in self.animation:
                self.clear()
                print(frame)
                time.sleep(0.5)

        self.clear()

        print(self.main)
