# Operators in Python
#There are several types of operators
#1. Arithmatic Operator => +,-,*,/,%,//,**
#2. Assignment Operator => =,+=,-=,*=,/=,*=,//=,**=
#3. Logical Operator => and, or, not
#4. Comparision or Relational Operator => ==,!=,<,>,<=,>=
#5. Identity Operator => is , isnot
#6. Membership Operator => in, innot

# Arithmatic Operator => +,-,*,/,%,//,**

# a = 10
# b = 20

# print(a+b)
# print(a-b)
# print("Hello"+"Python")
# print(str(a) + "Python")
# print(a*b)
# print(a/b)
# print(a%b)
# print(50%2)
# print(a//b) point pehla ni value consider kare
# print(7**2)

#Assignment Operator => =,+=,-=,*=,/=
# a = 10
# a = a + 10
# a-=5
# a*=10
# a/=2
# a//=3
# a**=2
# print(a)

#Logical Operator => and, or , not

#and Operator :-
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

#or Operator :-
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

#not Operator :-
# print(not False)
# print(not True)

#Real life example
# username = "admin"
# password = "admin1"

# print(password=="admin" and username=="admin")


#Comparision Operator :- ==,!=,<,>,<=,>=
# a = 10
# b = 20
# c = 10

# print(a==b)
# print(a!=b)
# print(a<b)
# print(a>b)
# print(a<=c)
# print(a>=b)

#Identity Operator => is, isnot

# a = 10
# b = 10

# print(a is b)

#list example
# a = [10,20]
# b = [10,20]
# c = a
# a.append(50)

# print(a)
# print(b)

# print(a is c)
# print(a is not b)

#Membership Operator => in, not in
# a = [10,20,30]
# print(100 in a)

#tuple example in identity
a = (10,20)
b = (10,20)

print(a is b)