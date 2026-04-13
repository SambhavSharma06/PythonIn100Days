# Single Inheritance in Python!!

class Animal:
    def __init__(self, name,species):
         self.name = name
         self.species = species

    def make_sound(self):
        print("Sound made by the animal.")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="dog")
        self.breed = breed

    def make_sound(self):
        print("Sound made by the dog.")

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Cat")
        self.breed = breed

    def make_sound(self):
        print("Sound made by the Cat.")

d = Dog("Dog","Sam")
d.make_sound()

a = Animal("Animal","dog")
a.make_sound()

#Quiz
C = Cat("Cat","CAT")
C.make_sound()
