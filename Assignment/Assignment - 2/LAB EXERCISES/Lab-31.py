#Aim :- Write a Python program to apply the map() function to square a list of numbers. 

my_items = [10,20,30,40,50,60]

k = map(lambda i : i*i,my_items)
print(list(k))