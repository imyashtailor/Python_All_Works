#Aim :- Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).

try:
    a = int(input("Enter the Number of a = "))
    b = int(input("Enter the Number of b = "))

    choice = int(input("Enter Your Choice = "))

    match choice:
        case 1:print("Addition is = ",a+b)
        case 2:print("Subtraction is = ",a-b)
        case 3:print("Multiplication is = ",a*b)
        case 4:print("Division is = ",a/b)
        case 5:print("Floor Division = ",a//b)
        case 6:print("Expotential = ",a**b)
        case _:print("Invalid Input")

except Exception as e:
    print(e)

finally:
    print("Program always Executed!....")