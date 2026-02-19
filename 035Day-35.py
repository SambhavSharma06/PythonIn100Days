#For Loop with else in Python!!

# REMEMBER ELSE IS ONLY WORKING BECAUSE THE LOOP IS SUCCESSFULLY END
# NOT BECAUSE IT IS BREAK OR SOMETHING
# for i in range(5):
#     print(i)
# else:
#     print("Sorry no i")

for i in range(6):
    print(i)
    if i ==4:
        break

else:
    print("Sorry no i")