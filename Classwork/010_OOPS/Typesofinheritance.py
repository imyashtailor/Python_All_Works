#Single Inheritance :-

# class A:
#     def sample(self):
#         self.s1 = input("Enter String 1 = ")

# class B(A):
#     def sample2(self):
#         self.s2 = input("Enter string 2 = ")
    
#     def concat(self):
#         print("Concatenation of Two Strings are = ",self.s1+" "+self.s2)

# b = B()
# b.sample()
# b.sample2()

# b.concat()


#Multiple Inheritance :-

# class A():
#     def test(self):
#         self.num = int(input("Enter Number = "))

# class B():
#     def test1(self):
#         self.num1 = int(input("Enter Number 1 = "))

# class C(A,B):
#     def test2(self):
#         self.num2 = int(input("Enter Number 2 = "))

#     def add(self):
#         print("Addiiton is = ",self.num + self.num1 + self.num2)

# c1 = C()
# c1.test()
# c1.test1()
# c1.test2()

# c1.add()


#Herarchical inheritance 

# class Car:
#     def __init__(self,name,color,model):
#         self.name = name
#         self.color = color
#         self.model = model
    
#     def display(self):
#         print(self.name,self.color,self.model)

# class Bike(Car):
#     def __init__(self, name, color, model):
#         super().__init__(name, color, model)

# class Cycle(Car):
#     def __init__(self, name, color, model):
#         super().__init__(name, color, model)

# b = Bike("Pulsar","Black","1500cc")
# c = Cycle("Downhill","Gray","simple")

# b.display()
# c.display()

#Multilevel Inheritance :-

# class A:
#     def test(self):
#         print("Class A")
# class B(A):
#     def show(self):
#         print("Class B")
# class C(B):
#     def display(self):
#         print("Class C")

# obj = C()
# obj.test()
# obj.show()
# obj.display()

#Hybrid Inheritance

class Vehicle:
    def __init__(self,name,price,brand):
        self.name = name
        self.price = price
        self.brand = brand
    
    def display(self):
        print(self.name,self.price,self.brand)

class Car(Vehicle):
    def __init__(self, name, price, brand):
        super().__init__(name, price, brand)

class Bike(Vehicle):
    def __init__(self, name, price, brand):
        super().__init__(name, price, brand)
    
class Cycle(Car,Bike):
    def __init__(self, name, price, brand):
        super().__init__(name, price, brand)

c1 = Car("Bugati",12345,"Bugati")
b1 = Bike("Activa",90000,"Honda")
c2 = Cycle("Downhill",45000,"Zipper")

c1.display()
b1.display()
c2.display()

