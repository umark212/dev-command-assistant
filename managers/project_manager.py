from pathlib import Path


class ProjectManager:

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
