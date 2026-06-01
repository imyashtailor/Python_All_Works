import re

#Only check the digit
# number = input("Enter Number = ")

# k = re.match(r"^[0-9]{10}$",number)
# if k is None:
#     print("Invalid Number")
# else:
#     print(number)

#only check alphabetical

# message = input("Enter Message = ")

# k = re.match(r"^[a-z]{8}$",message)
# if k is None:
#     print("Invalid message")
# else:
#     print(message)


#email pattern programming :-

# email = input("Enter the email = ")

# k = re.match("^[a-z0-9_-]+@[a-z]+\\.[a-z]{2,4}$",email)
# print(k)

# Tasks :-
#password checking
#at least one capital, small, number and also a one special charcter and range(8)

password = input("Enter the Password = ")

p = re.match(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@!&*_])[A-Za-z\d@!&*_]{8,15}",password)
print(p)
if p:
    print("Match the password")
else:
    print("Match Not Found")

