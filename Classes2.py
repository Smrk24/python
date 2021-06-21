class Car:
    """Attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initialite atributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year

 
redCar = Car("Skoda", "Felicia", 1998)
yellowCar = Car ("Skoda", "Favorit", 1988)


print (redCar.make, redCar.model, "is the best car ever")
print (f"{yellowCar.make} {yellowCar.model} is worse than {redCar.make} {redCar.model}")