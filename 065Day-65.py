#Static Methods in Python!!

class Area:
    staticmethod
    def AreaOfCircle(r):
        return 3.14*r**2
    def AreaOfRectangle(l,b):
        return l*b
    def AreaOfTriangle(l,h):
        return 0.5*(l*h)
print(Area.AreaOfCircle(5))
print(int((Area.AreaOfRectangle(5,7))))
print(Area.AreaOfTriangle(5,5))


