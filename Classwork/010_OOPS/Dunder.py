#Dunder method :- object na representation mate use thy 

#1. __str__ method :- define a human redable string for print() or str()
class Demo:
    name = "yash"
    def __str__(self):
        return self.name

d = Demo()
print(d)

#2. __eq__ method :- defines the equality checking for the == operator
class calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __eq__(self, value):
        return self.a == value.a and self.b == value.b

c = calc(10,20)
c1 = calc(10,20)
print(c==c1)

#3.__len__ method :- return the length when calling len(object)

class Test:
    def __init__(self,a):
        self.a = a

    def __len__(self):
        return len(self.a)

t = Test([10,20,30,40,50])
print(len(t))

#4. __setitem__ :- it is a dunder method used when you assign a value using square bracket[]
class Test1:
    def __init__(self,a):
        self.a = a

    def __setitem__(self, key, value):
        self.a[key] = value

t1 = Test1([10,20,30,40,60])
t1[2] = 77
print(t1.a)

#5 .__getitem__ :-Allows a indexing like obj[key]

class Test2:
    def __init__(self,a):
        self.a = a
    
    def __getitem__(self, key):
        return self.a[key]

t2 = Test2([23,45,67,89,55])
print(t2[1])