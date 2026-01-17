#String Methods in Python!!

str1 = "Hello, World!"
print(str1.upper())
print(str1.lower())

str2 = "   Python Programming   "
print(str2.strip())

str3 = "Hello, World!!!"
print(str3.rstrip("!"))

print(str1.replace("World", "Python"))

print(str1.split(", "))

str5 ="hello"
cap_str5 = str5.capitalize()
print(cap_str5)

str6 = "welcome to python programming"
print(str6.center(40, '*'))

str7 = "Python is fun fun fun"
print(str7.count("fun"))

str8 = "I love Python"
print(str8.endswith("Python"))
print(str8.endswith("love", 2, 6))

str9 = "Python3"
print(str9.find("3"))

#-1 if it doesnt find the value btw!!!

str10 = "He's a programmer"
print(str10.index("programmer"))

#As we can see, this method is somewhat similar to the find() method.
# The major difference being that index() raises an exception if value is absent whereas find() does not.

str11 = "IAmSambhav"
print(str11.isalnum())
print(str11.isalpha())
print(str11.islower())
print(str11.printable())
print(str11.isspace())

str12 = "Welcome To Python"
print(str12.istitle())
print(str12.isuppper())
print(str12.startswith("Welcome"))
print(str12.swapcase())
print(str12.title())




