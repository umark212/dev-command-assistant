#assistant, all functions to be added here.

from managers.project_manager import ProjectManager
from managers.file_manager import FileManager
from managers.text_manager import TextManager
from logger import Logger

class DeveloperAssistant:

    def __init__(self):  #because we're accessing other classes

        self.projects = ProjectManager()
        self.files = FileManager()
        self.text = TextManager()
        self.logger = Logger()
    


    

