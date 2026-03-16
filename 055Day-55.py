#Snake Water Gun in Python!
import random

choices = ["snake", "water", "gun"]

computer = random.choice(choices)
user = input("Choose snake, water, or gun: ").lower()

print("Computer chose:", computer)

if user not in choices:
    print("Invalid choice")
elif user == computer:
    print("It's a draw!")
elif (
    (user == "snake" and computer == "water") or
    (user == "water" and computer == "gun") or
    (user == "gun" and computer == "snake")
):
    print("You win!")
else:
    print("Computer wins!")
