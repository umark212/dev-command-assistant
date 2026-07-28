from datetime import datetime #using datetime library as its helpful for getting current date and time

class Logger:

    def log(self, action):
        with open("rushmore.log", "a", encoding="utf-8") as file:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #datetime.now gets current time/date and .strftime() converts that object into string i formatted
            file.write(f"[{time}] {action}\n")
