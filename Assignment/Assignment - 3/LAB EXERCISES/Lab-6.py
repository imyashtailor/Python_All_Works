#Aim :- Write a Python program to write multiple strings into a file. 

with open('demo.txt','w') as f:
    my_str = ["Hello\n","Python\n","Hello\n","Java\n"]
    f.writelines(my_str)