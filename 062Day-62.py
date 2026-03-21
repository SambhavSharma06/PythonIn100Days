#Access Modifiers in Python!!

class Employee:
    def __init__(self):
        self.__name = "Harry"

a = Employee()
# print(a.__name)
print(a._Employee__name)#Can be accessed indirectly.
