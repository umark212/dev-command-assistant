import subprocess  #module which allows python to run other programs installed on computer


class GitManager:

    def initialise(self, project_path):  #method needs to know where project is located
        try:
            result = subprocess.run(
                ["git", "init"], #using list: first item is program (git) second item is argument given to that program (init)
                cwd=project_path #runs git init inside this projects folder
                capture_output=True, 
                text=True  #get output from git and make it text instead of bytes
            )

        
            if result return.code == 0:    #git rule: if output 0 it means initialisation was successful, otherwise it means it failed, so return true to project manager
                print("Git repository initialised successfully.")
                return True

            print(f"Git initialisation failed: {result.stderr}") #result.stderr is where error messages stored
            return False

        except: FileNotFoundError:
            print("Git is not installed or is not available in PATH.")
            return False
