#Aim :- Write a Python program to read the contents of a file and print them on the console. 

f = open('demo.txt','r')
content = f.read()
print(content)
f.close()