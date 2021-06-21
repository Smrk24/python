class Restaurant():
    """A class representing a restaurant"""
    def __init__(self, name, cuisineType):
        """Initialize the restaurant"""
        self.name = name
        self.cuisineType = cuisineType

    def describeRestaurant(self):
        """Display a summary of the restaurant"""
        print (f"{self.name} has the best {self.cuisineType}")
        
myRestaurant = Restaurant ("Pepe's Pasta", "Spaghetti")
print (myRestaurant.name)
print (myRestaurant.cuisineType)

myRestaurant.describeRestaurant ()

