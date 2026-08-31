class Robot:
    # Constructor
    def __init__(self, name, color, purpose):
        self.name = name
        self.color = color
        self.purpose = purpose

    # Method to introduce the robot
    def introduce(self):
        print("Hello! I am a robot.")
        print("My name is", self.name)
        print("My color is", self.color)
        print("My purpose is to", self.purpose)


# Creating an object
robot1 = Robot("Robo", "Blue", "help humans")

# Calling the method
robot1.introduce()