#Solutions and Shoutouts in Python

st = input("Enter a message: ")
words = st.split(" ")

mode = input("Type 'c' to CODE or 'd' to DECODE: ")

nwords = []

if mode == 'c':  # CODING
    for word in words:
        if len(word) >= 3:
            r1 = "dsf"
            r2 = "jkr"
            new_word = r1 + word[1:] + word[0] + r2
            nwords.append(new_word)
        else:
            nwords.append(word)

elif mode == 'd':  # DECODING
    for word in words:
        if len(word) >= 3:
            # remove dsf and jkr
            word = word[3:-3]
            # move last letter to front
            new_word = word[-1] + word[:-1]
            nwords.append(new_word)
        else:
            nwords.append(word)

else:
    print("Invalid choice! Please enter 'c' or 'd'.")
    exit()

print("Result:", " ".join(nwords))
