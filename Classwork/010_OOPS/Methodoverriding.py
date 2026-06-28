# Method Overriding :- parent to class and same name but differnt body that is known as Method Overriding

class A:
    def test(self):
        print("Test calling of A")

class B(A):
    def test(self):
        print("Test calling of B")
        super().test() #both messages are print => (both message ne print karva mate)

b = B() 
b.test()