# Regular Expressions in Python!!

import re

Finder = "was"

text = "My name is Sambhav Sharma and I was 19 years old last year"

Answer = re.search(Finder, text)
print(Answer)