#Function Arguments in Python!!

def name(fname,mname= "John", lname="Whatson"):
    print("Hello", fname, mname, lname)
    
    name("Sherlock") #Default Argument


def age(age1,age2,age3):
    print("Age is:", age1, age2, age3)  
    
age(age1=30, age2=35, age3=32) #Keyword Argument  

def city(city1, city2, city3):
    print("City is:", city1, city2, city3)
city("London", "New York","Delhi") # Required Argument

def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes") #Arbitrary Argument

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James") #Arbitrary Keyword Argument

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes")) #Return Statement