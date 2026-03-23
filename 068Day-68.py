#Clear the clustar in Python!!

import os

files = os.listdir("DAYS_OF_PYTHON")

i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"DAYS_OF_PYTHON/{file}", f"DAYS_OF_PYTHON/{file}.png")
        i = i + 1