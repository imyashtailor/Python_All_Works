# Aim :- Create a mini-project where students combine conditional statements, loops, and functions 
# to create a basic Python application, such as a simple calculator or a grade management 
# system. 

#simple Calculator using functions
# def calc():
#     print("========Simple Calculator========")

#     a = int(input("Enter the Number 1 = "))
#     b = int(input("Enter the Number 2 = "))

#     choice = "y"
#     while choice!="n":
#         ch = input("Enter Your choice = ")
#         match ch:
#             case "1": print("Addition is = ",a+b)
#             case "2": print("Subtraction is = ",a-b)
#             case "3": print("Multiplication is = ",a*b)
#             case "4": print("Division is = ",a//b)
#             case _: print("Invalid Choice")

#         choice = input("Do you want to continue? (y/n) = ")
#         if choice == 'n':
#             print("Good Bye!..See You Tomorrow")

# #call the function
# calc()








#Simple Grade Management System using function

def grade_system():
    print("======Simple Grade Management System========")

    n = int(input("Enter number of subjects = "))
    total=0

    for i in range(n):
        marks = float(input(f"Enter marks of subjects {i+1} = "))
        total+=marks
    
    print("Total Marks = ",total)

    avg = total / n
    print("Average Marks = ",avg)

    if avg>=75:
        print("Grade = Distinction")
    elif avg>=60:
        print("Grade = First Class")
    elif avg>=40:
        print("Pass")
    else:
        print("Fail")


#call the functioin
grade_system()


