
#check and find prime numbers
# isprime=1
# num = int(input("Enter the Numnber = "))

# if num<=1:
#     isprime=0
# else:
#     for i in range(2,num):
#         if num % i == 0:
#             isprime=0
#             break

# if isprime==1:
#     print(f"{num} is Prime")
# else:
#     print(f"{num} is Not Prime")


# print 3 to 100 prime numbers
# count=0
# for j in range(3,100):
#     number = j
#     flag = 0
#     for i in range(3,number):
#         if number % i == 0:
#             flag = 1
#             break
    
#     if flag == 0:
#         print(f"{number} is prime number")
#         count+=1
    

# print(f"Total Prime Numbers are = ",count)

count=0
n = int(input("Enter the Number = "))
print(f"All Prime Numbers Between 3 to 100 are = ",n)

for num in range(3,n):
    flag=1

    for i in range(3,num):
        if num % i == 0:
            flag=0
            break

    if flag==1:
        print(num)
        count+=1

print(f"Total Prime Numbers are = ",count)