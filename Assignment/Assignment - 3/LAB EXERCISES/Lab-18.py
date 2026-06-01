#Aim :- Write a Python program to match a word in a string using re.match().

import re

text = "Car is very beautiful"

k = re.match("Car",text)
print(k)
if k:
    print("Match Found")
else:
    print("Match not Found")