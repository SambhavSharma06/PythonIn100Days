# Raise ValueError Python!!

a = input("Enter any value between 5 and 9 (or type 'quit'): ")

if a == "quit":
    print("Exiting…")
else:
    a = int(a)  # now safe to convert
    if a < 5 or a > 9:
        raise ValueError("Value is not an accepted value")

print("Accepted:", a)
