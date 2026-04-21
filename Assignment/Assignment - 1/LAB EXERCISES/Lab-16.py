#Aim :- Write a Python program to skip 'banana' in a list using the continue statement. List1 = ['apple', 'banana', 'mango']

fruits = ['Apple','Banana','Mango']

for fruit in fruits:
    if fruit == 'Banana':
        continue
    print(fruit)