#Exercise 1: Calculator using Python!!
#CALCULATOR
print("Welcome to the Calculator Program")
print("Select operation:"
      "\n1.Addition For adittion type +"
      "\n2.Subtraction For subtraction type -"
      "\n3.Multiplication For multiplication type *"
      "\n4.Division For division type /"
      "\n5.Exit For exit type EXIT")
print(input("Enter operation: "))

if(input=='+'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print("The result is: ", result)
elif(input=='-'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 - num2
    print("The result is: ", result)
elif(input=='*'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 * num2
    print("The result is: ", result)
elif(input=='/'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("The result is: ", result)
elif(input=='EXIT'):
    print("Exiting the Calculator Program. Goodbye!")
    print(exit)
else:
    print("Invalid input")




