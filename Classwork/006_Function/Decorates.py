#Decoraters :- function ma original karya vagar aapne amuk changes karvu 
#Definition :- A Decorator in Python is a function that adds extra functionality to another function 
# without changing its original code.

# def after(func):
#     def execute():
#         func()
#         print("Calling after test")
#     return execute

# def before(func):
#     def execute():
#         print("Calling Before test")
#         func()
#     return execute

# @after
# @before

# def test():
#     print("hello world")

# test()



#create a decorattor for functions with paramater

# def add(func):
#     def execute(*a):
#         print("Addition below")
#         sum = 0
#         for i in a:
#             sum+=i
#         print("Addition is = ",sum)
#         func(*a)
#     return execute

# def mul(func):
#     def execute(*a):
#         print("Multiplication below")
#         sum = 1
#         for i in a:
#             sum*=i
#         print("Multiplication is = ",sum)
#         func(*a)
#     return execute

#function with paramaeter
# @add
# @mul
# def calc(a,b):
#     pass

# calc(20,30)


#Task :- 

# def numbersonly(func):
#     def execute(a):
#         if str(a).isdigit():
#             func(a)
#         else:
#             print("Invalid Input")
#     return execute

def onlyalpha(func):
    def execute(a):
        if str(a).isalpha():
            func(a)
        else:
            print("Invalid Input1")
    return execute

# @numbersonly
@onlyalpha
def get(a):
    print(a)
get(10)

