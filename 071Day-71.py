#dir, __dict__ and help method in Python!!
#x = [1,2,3]
# x = (1,2,3)
# print(dir(x))
# print(x.__add__)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1
p = Person("Sam", 500,)
print(p.__dict__)

print(help(Person))
