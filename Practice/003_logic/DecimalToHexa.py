num = int(input("Enter the Number = "))
reve=""

l = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

while num!=0:
    digit = num % 16
    reve = l[digit] + reve
    num = num // 16

print(reve)