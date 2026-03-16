#Lambda functions in Python

cube = lambda x: x**3
print(cube(5))

def SamKal(fx,value):
    return 6 + fx(value)
print(SamKal(cube,6))
