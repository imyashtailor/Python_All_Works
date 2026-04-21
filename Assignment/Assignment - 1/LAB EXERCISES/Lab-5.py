#Aim :- How to create variables in Python? 

#write a program to create a Armstrong Number

# varaible = num,digit,sum,temp

num = int(input("Enter the Number = "))

temp = num
sum=0

while temp!=0:
    digit = temp % 10
    sum = sum + (digit*digit*digit)
    temp = temp // 10 #for integer to use (//)

if sum==num:
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong Number")