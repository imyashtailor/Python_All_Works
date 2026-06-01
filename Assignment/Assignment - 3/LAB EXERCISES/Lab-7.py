#Aim :- Write a Python program to check the current position of the file cursor using tell().

with open('demo.txt','r') as f:
    print("Start position = ",f.tell())

    f.read(5)

    print("After reading 5 Characters = ",f.tell()) 