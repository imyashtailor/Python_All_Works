#Aim :- Write a Python program to create a calculator using functions. 

def calc():
    a = int(input("Enter Number 1 = "))
    b = int(input("Enter Number 2 = "))

    choice = "y"
    while choice!="n":
        ch = int(input("Enter Your Choice = "))

        match ch:
            case 1:print("Addition is = ",a+b)
            case 2:print("Subtraction is = ",a-b)
            case 3:print("Multiplication is = ",a*b)
            case 4:print("Division is = ",a//b)
            case _: print("Invalid operations!..")
        
        choice = input("Do you want to continue? (y/n) = ")

#call the function
calc()