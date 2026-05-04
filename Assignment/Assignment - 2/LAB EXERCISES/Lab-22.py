#Aim :- Write a Python program to count how many times each character appears in a string.

text = "Hello Python"

count = {}

for char in text:
    count[char] = count.get(char,0)+1

print(count)