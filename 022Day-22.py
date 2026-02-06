#List in Pythons!!

Name = ["Sam, John, Peter, Paul"]
print(Name)

AgeAndName = ["Sam", 25, "John", 30, "Peter", 28]
print(AgeAndName)

print(AgeAndName[0])

print(AgeAndName[-3])#Remember negative indexing starts from -1

if "Sam" in Name:
    print("Yes, Sam is in the list")
else:
    print("No, Sam is not in the list")

#ListName[start:stop:step]

print(AgeAndName[0:6:2])

#List Comprehension:-

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)