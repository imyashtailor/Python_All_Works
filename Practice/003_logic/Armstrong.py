
for i in range(100,1000):
    sum=0
    num = i

    temp = num

    while num!=0:
        digit = num % 10
        sum+=(pow(digit,3))
        num = num // 10

    if temp==sum:
        print(f"{temp} is an Armstrong Number")
    else:
        pass

