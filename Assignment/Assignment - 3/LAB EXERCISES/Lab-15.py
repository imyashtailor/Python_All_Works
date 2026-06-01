#Aim :-  Write a Python program to show method overloading.

from multipledispatch import dispatch
class calc():
    @dispatch(int,int)
    def mul(self,a,b):
        print(f"Multiplication of {a} and {b} is {a*b}")
    
    @dispatch(int,int,int)
    def mul(self,a,b,c):
        print(f"Multiplication of {a}, {b} and {c} is {a*b*c}")

c = calc()
c.mul(10,20)
c.mul(10,20,30)


