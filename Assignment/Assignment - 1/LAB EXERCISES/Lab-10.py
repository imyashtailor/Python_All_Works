# Aim :- Write a Python program to calculate grades based on percentage using if-else ladder. 
# conditions :-
# percentage < 0 or percentage > 100 → Invalid input
# 90–100 → A+
# 80–89 → A
# 70–79 → B
# 60–69 → C
# 50–59 → D
# < 50 → F

per = float(input("Enter the Percentage = "))

if per < 0 or per > 100:
    print("Invalid Input!...")
if per >=90 and per <=100:
    print("Grade A+")
elif per>=80 and per <=89:
    print("Grade A")
elif per>=70 and per <=79:
    print("Grade B")
elif per>=60 and per <=69:
    print("Grade C")
elif per>=50 and per <=59:
    print("Grade D")
elif per<=50:
    print("Grade F")