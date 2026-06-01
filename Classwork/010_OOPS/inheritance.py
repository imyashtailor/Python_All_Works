class A:
    id = 10
    def test(self):
        print("Class A calling")

class B(A):
    id = 50
    def sample(self):
        print(self.id)
        print(A.id)  #ek j class ma parent class ne refer karva mate
        # print(super().id) # second way to refer a parent class

b = B()
b.sample()
b.test()

