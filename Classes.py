class animal:
    """"A simple attempt to model a Duck """

    def __init__(self, name, age):
        """"Initialize name and age attributes"""
        self.name = name
        self.age = age


    def sit(self):
        """simulate a duck sitting in response to a command"""
        print (f"{self.name} is now sitting")

    def roll_over(self):
        """simulate a ducking roll over in response to a command"""
        print(f"{self.name} ducked over")

my_duck = animal("Ivan", 4*2)
ales_python = animal ("Annie", 14)

print(f"My duck is {my_duck.name}")
print(f"{my_duck.name} is {my_duck.age}")
print(f"Aleš's python is {ales_python.name}")
print(f"{ales_python.name} is {ales_python.age}")


