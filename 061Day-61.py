#Inheritance in Python!!

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def ShowLanguage(self):
        print(f"The default language is Python")


e1 = Employee("Rohan Das",1)
e1.showDetails()
e2 = Employee("Harry",2)
e2.showDetails()
e3 = Programmer("Sambhav",3)
e3.ShowLanguage()
