#functions 

#create a function
#function without paramater
def message():
    print("hello world")

message()
# message()

#function with single parameter
def add1(a):
    print(f"the square of {a} is {a*a}")

add1(5)

#function with parameter
def sum(a,b):
    print(f"addition of {a} and {b} is {a + b}")

sum(30,50)

#function with return type
# a data-type of value a function 
def cube(a):
    q = a*a*a
    return q

q = cube(10)
print(q)
print(cube(4))

#create a functions for factorial

# def factorial():
#     num = int(input("Enter the Number = "))
#     fact = 1

#     for i in range(num,0,-1):
#         fact = fact * i
    
#     print(f"factorial of given number is = ",fact)

# factorial()

#deafult argument
def person(name,email="abc@gmail.com",age=25):
    print(name,email,age)

person("yash",age=45) #keyword argument

#arbitory argument => single element mate multiple addition kari sakiye
# single * mate  
def add(*a):
    sum=0
    for i in a:
        sum+=i
    print(sum)

add(10,20,60,80)

#key-value pair ma data joyta hoi to use karvu (multiple data mate)
#dictonary mate use karay
#arbitory argument
def person(**k):
    print(k)

person(name="yash",email="xyz",age=25)


#lamda function => function without name, single time use karva mate(ek j var use karva mate)
mul = lambda a,b : a*b
print(mul(20,6))

square = lambda p : p*p
print(square(6))