# def square(a):
#     print(a*a)
#     a+=1
#     if a<20:
#         square(a)

# square(1)


#write a program to find factorial using recursion

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

num = int(input("Enter the Number = "))

if num < 0:
    print("Factorial not defined for negative numbers")
else:
    result = fact(num)
    print("Factorial of given number is =", result)