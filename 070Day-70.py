#Class methods as alternative constructors in Python!!

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromStr(cls, string):
         return cls(string.split("-")[0], string.split("-")[1])
e1 = Employee("Sam", 5000)
print(e1.name)
print(e1.salary)

string = "John-12000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)
