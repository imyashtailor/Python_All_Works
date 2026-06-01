#Aim :- Write a Python program to show method overriding. 

class A:
    def test(self):
        print("Test calling of A")

class B(A):
    def test(self):
        print("Test calling of B")
        # super().test() #both messages are print => (both message ne print karva mate)

b = B()
b.test()