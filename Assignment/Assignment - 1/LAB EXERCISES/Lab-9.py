#Aim :- Write a Python program to check if a number is prime using if_else.

isprime=1
num = int(input("Enter the number = "))

if num<=1:
    isprime=0
else:
    for i in range(2,num):
        if num % i == 0:
            isprime=0
            break

if isprime==1:
    print("It is a prime number")
else:
    print("It is not a prime number")

