# Multilevel Inheritance in Python!!
# Base class
class Grandfather:
    def house(self):
        print("Grandfather has a house")

# Inherits from Grandfather
class Father(Grandfather):
    def car(self):
        print("Father has a car")

# Inherits from Father (and indirectly Grandfather)
class Son(Father):
    def bike(self):
        print("Son has a bike")

# Create object of Son
obj = Father()

obj.house()   # From Grandfather
obj.car()     # From Father
