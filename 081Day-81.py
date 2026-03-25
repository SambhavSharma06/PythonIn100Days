# Hybrid and Hierarchical Inheritance in Python!!

class A:
    def showA(self):
        print("Class A")

class B(A):  # Inheriting A (single inheritance)
    def showB(self):
        print("Class B")

class C(A):  # Inheriting A (hierarchical part)
    def showC(self):
        print("Class C")

class D(B, C):  # Multiple inheritance (hybrid formed)
    def showD(self):
        print("Class D")

# Object creation
obj = D()

obj.showA()
obj.showB()
obj.showC()
obj.showD()