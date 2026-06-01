# Operator Overloading :- using dundar method
#Operator overloading in python that allows same operator to work in different ways depending on data type that is 
#known as Operator overloading
#using dunder method (__add__, __mul__,__init__) examples

class calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __add__(self, other):
        return self.a + other.a, self.b + other.b

    def __mul__(self, other):
        return self.a * other.a, self.b * other.b

c = calc(10,20)
c1 = calc(30,40)

k = c + c1
print(k)