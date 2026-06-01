#method overloading does not support in python
#but jo tamare karvu hoi to third party thi kari sako (strict rite) multipledispatch thi
#Method Overloading :- same name but different parameter that is known as method overloaidng 

from multipledispatch import dispatch

class calc:
    @dispatch(int,int)
    def add(self,a,b):
        print(f"Addition of {a} and {b} is {a+b}")
    
    @dispatch(int,int,int)
    def add(self,a,b,c):
        print(f"Addition of {a} , {b} and {c} is {a+b+c}")

c = calc()
c.add(10,20)
c.add(10,20,30)