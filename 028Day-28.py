# F-Strings in Python!!
letter = "Hey my name is { } and I am from { }" 
Country = "India" 
name = "Harry"

print(f" Hey my name is {name} and I am from {Country}")

price = 49.99999999
txt  = f" For only {price:.2f} dollars!"
print(txt)
print(type(txt)) 
print(f"{{ {name} }}")  # To print curly braces
