#octal to decimal
sum=0
p=0
num = int(input("Enter the Number = "))

while num!=0:
    digit = num % 10
    sum+=(digit*pow(8,p))
    num = num // 10
    p+=1    

print(f"Octal Number is {sum}")