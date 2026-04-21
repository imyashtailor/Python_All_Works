# num = int(input("Enter the Number = "))
# fact=1

# for i in range(num,0,-1):
#     fact = fact*i
    
# print(f"Factorial of given Number is = ",fact) 

#using while loop

num = int(input("Enter the Number = "))
fact=1

while num > 0:
    fact = fact*num
    num = num - 1 

print(f"Factorial of Given Number are = ",fact)