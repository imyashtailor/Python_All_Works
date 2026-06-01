#Aim :- Write a Python program to search for a word in a string using re.search().

import re

text = "Python is easy"

k = re.search("as",text)
print(k)
if k:
    print("Match Found")
else:
    print("Match not Found")