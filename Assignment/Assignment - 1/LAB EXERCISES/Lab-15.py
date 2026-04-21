# Aim :- Print this pattern using nested for loop
# * 
# ** 
# *** 
# **** 
# *****

lines = 5

for i in range(lines):
    for j in range(i+1):
        print("*",end="")
    print()