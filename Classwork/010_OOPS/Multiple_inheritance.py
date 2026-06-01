class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print('a cons calling')
    
    def display(self):
        print(self.x,self.y)
        # print("A display calling")

class B:
    def __init__(self,x,y,z):
        self.x=  x
        self.y = y
        self.z = z
        print("B cons calling")
    
    def display(self):
        print(self.x,self.y,self.z)
        # print("B is calling")

class C(A,B):
    def __init__(self, x,y,z):
        super().__init__(x,y,z)

c = C(10,20,30)
c.display()
