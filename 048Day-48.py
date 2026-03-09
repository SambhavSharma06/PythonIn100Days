#Local vs Global Variables in Python

x = 10 # Global Variable

def my_function():
    global x
    x = 4
    y = 5 # Local Variable
    print(y)

my_function()
print(x)
#print(y)#This will cause an error because y is a local
        #local variable and is not accessible outside
        #of the function