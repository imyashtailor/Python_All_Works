rev=0
num = int(input("Enter the Number = "))

temp = num

while num!=0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp==rev:
    print(f"{temp} is Palindrome Number")
else:
    print(f"{temp} is not an Palindrome Number")
