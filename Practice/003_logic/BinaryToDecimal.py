sum=0
p=0
num = int(input("Enter the Number = "))

while num!=0:
    digit = num % 10
    sum+=(digit*pow(2,p))
    num = num // 10
    p+=1

print(sum)