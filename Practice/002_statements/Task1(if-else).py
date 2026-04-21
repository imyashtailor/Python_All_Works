#Grade Task

marks = int(input("Enter the Marks = "))

if marks>100:
    print("Invalid Marks Obtained!...")

if marks > 90 and marks <= 100:
    print("Grade A")
elif marks > 70 and marks <=90:
    print("Grade B")
elif marks > 50 and marks <=70:
    print("Grade C")
elif marks > 30 and marks <=50:
    print("Grade D")
elif marks > 0 and marks <=34:
    print("Grade F")
else:
    print("Something Went wrong")

# num = int(input("Enter the Number = "))
# if num>0:
#     if num % 2 == 0:
#         print("Positive and Even Number")
#     else:
#         print("Negative and Odd Number")
# else:
#     print("Number is Negative")