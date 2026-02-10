#Docstrings in Python!!
import this #The Zen of Python
def square(n): 
    '''Takes in a number n,returns the square of n''' #Docstring
    print(n**2)
    square(5)
print(square.__doc__)