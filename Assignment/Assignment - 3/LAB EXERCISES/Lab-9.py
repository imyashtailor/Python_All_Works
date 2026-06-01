#Aim :- Write a Python program to demonstrate handling multiple exceptions. 

try:
    a = int(input("Enter the number 1 = "))
    b = int(input("Enter the number 2 = "))

    res = a / b

    my_list = [10,20,30]
    print("Element = ",my_list[5])

    print("Result = ",res)

except ValueError:
    print("Please enter valid integers")

except ZeroDivisionError:
    print("Zero division is not allowed!...")

except IndexError:
    print("Value is Out of the range")

finally:
    print("Always Execute....")