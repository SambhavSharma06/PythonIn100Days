# Simple KBC Game Python!!
print("Welcome to KBC")

Questions = ["What is the capital of India?", "What is 2+2?"]

# Question 1
print(Questions[0])
optionsFor1 = ["1. Mumbai", "2. New Delhi", "3. Chennai"]
print(optionsFor1)

answer1 = int(input("Enter the correct option number: "))

if answer1 == 2:
    print("Correct Answer!")
    print("You won 100$")
else:
    print("Wrong Answer!")
    print("Game Over")
    exit()

# Question 2
print(Questions[1])
optionsFor2 = ["1. 3", "2. 4", "3. 5"]
print(optionsFor2)

answer2 = int(input("Enter the correct option number: "))

if answer2 == 2:
    print("Correct Answer!")
    print("You won 200$")
    print("Thx for playing!!")
else:
    print("Wrong Answer!")
    print("Game Over")
