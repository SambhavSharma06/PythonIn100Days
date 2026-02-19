import random
import string

print("1. Code")
print("2. Decode")

choice = input("Enter 1 to Code, 2 to Decode: ")

# CODE

if choice == "1":
    word = input("Enter your word: ")

    # Swap first and last letters
    if len(word) > 1:
        swapped = word[-1] + word[1:-1] + word[0]
    else:
        swapped = word   # If word has 1 letter

    # Make 3 random letters for front
    front = "".join(random.choice(string.ascii_lowercase) for _ in range(3))

    # Make 3 random letters for back
    back = "".join(random.choice(string.ascii_lowercase) for _ in range(3))

    # Final coded word
    coded = front + swapped + back

    print("Coded word:", coded)


#DECODE


elif choice == "2":
    coded_word = input("Enter the coded word: ")

    # Remove first 3 and last 3 letters
    middle = coded_word[3:-3]

    # Swap back last and first letters
    if len(middle) > 1:
        decoded = middle[-1] + middle[1:-1] + middle[0]
    else:
        decoded = middle

    print("Decoded word:", decoded)

else:
    print("Invalid choice.")
