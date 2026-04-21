
# Area of circle :-

# pi = 3.14

# r = float(input("Enter the Radius = "))
# print(r)

# area = pi*r*r
# print("Area of Circle = ",area)

#Area of Rectangle :-

# w = float(input("Enter the Width = "))
# # print(w)

# l = float(input("Enter the length = "))
# # print(l)

# area = float(w * l)

# print("Area of Rectnagle = ",area)

#find a simple interest
# interest = (p*n*r) / 100

# p = int(input("Enter the Principle = "))
# n = int(input("Enter the No.of Year = "))
# r = int(input("Enter the Rate = "))

# interest = (float(p*n*r) / 100)
# print("Simple Interest = ",interest)

#Additin of two numbers
# a = 10
# b = 20
# print(a+b)

#prime numbers
isprime=1
num = int(input("Enter the Number = "))

if(num<=1):
    isprime=0
else:
    for i in range(2,num):
        if(num % i == 0):
            isprime=0
            break
    
    if(isprime==1):
        print("It is a prime number")
    else:
        print("It is not a prime number")


    