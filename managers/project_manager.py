from pathlib import Path
from config_manager import ConfigManager
from managers.git_manager import GitManager

class ProjectManager:

    def __init__(self, logger):
        self.logger = logger
        self.config = ConfigManager()
        self.git = GitManager()

    def create_project(self):
        project_name = input("Enter project name: ")

        project_directory = self.config.get("default_project_directory")

        if not project_directory:            #added json configuration so project created in current directory or configured folder
            project_directory = Path.cwd()

        project = Path(project_directory) / project_name
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

        self.logger.log(f"Created project '{project_name}'")


        if self.config.get("auto_git_init"):  #checks through config json file whether rushmore should initialise git automatically
            git_created = self.git.initialise(project) #t or f

                
        self.logger.log(f"Initialised Git repository for '{project_name}'")
