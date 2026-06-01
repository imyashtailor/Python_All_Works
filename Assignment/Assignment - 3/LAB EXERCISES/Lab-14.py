#Aim :- Write a Python program to demonstrate the use of super() in inheritance.

class A:
    def test(self):
        print("Class A Calling")

class B(A):
    def test(self):
        super().test()
        print("Class B Calling")

b = B()
b.test() 