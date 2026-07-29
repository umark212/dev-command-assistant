import subprocess  #module which allows python to run other programs installed on computer


class GitManager:

    def initialise(self, project_path):  #method needs to know where project is located
        subprocess.run(
            ["git", "init"], #using list: first item is program (git) second item is argument given to that program (init)
            cwd=project_path
        )
/
