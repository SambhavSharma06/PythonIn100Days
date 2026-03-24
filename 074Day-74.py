# Method Overriding in Python!!

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):          # overriding
        print("Dog barks")

a = Animal()
a.sound()

d = Dog()
d.sound()


