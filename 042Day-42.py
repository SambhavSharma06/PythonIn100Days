#Enumerate Function in Python!!

marks = [12,56,32,98,45,1,4]

for index, mark in enumerate(marks, start=3):
    print(mark)
    if index == 3:
        print(index, mark)