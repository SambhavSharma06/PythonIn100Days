#Exception Handling Python!!

a = input("Enter a number: ")
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1,11):
     print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
 print("Invalid Input!")

print("Some lines of code")
print("End of program")