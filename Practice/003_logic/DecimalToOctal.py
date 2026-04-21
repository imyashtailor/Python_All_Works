num = int(input("Enter the Number = "))
st = ""

while num!=0:
    digit = num % 8
    st = str(digit) + st
    num = num // 8

print(f"Decimal to Octal Number is = ",st)
