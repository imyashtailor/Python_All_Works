#__init__ :- iska kaam hi he constructor ko create karna
#classmethod = only class na data ne j refer kare
#staticmethod = only info leva mate
#constructor :- construcotr is a special method that is automatically called when you create instace of the class
#Attributes :- instance attribute



# class Student:

#     #creating a constructor
#     def __init__(self,name,email,age):
#         self.name = name
#         self.email = email
#         self.age = age

#     def display(self):
#         print(self.name,self.email,self.age)

# s1 = Student("Yash Tailor","yash123@gmail.com",25)
# s1.display()

# s2 = Student("Harsh Patel","harshu234@gmail.com",25)
# s2.display()



#Methods 
#classmethods :- only refer to the class data
#static methods :- koi info leva mate and work like a normal function

class Student:

    clg = "SNPIT"
    #creating a constructor
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age

    def display(self):
        print(self.name,self.email,self.age,self.clg)

    @classmethod
    def test(cls):
        print(cls.clg)
    
    @staticmethod
    def demo():
        print("Static calling")

Student.clg = "abc"

s1 = Student("Yash Tailor","yash123@gmail.com",25)
# s1.id = "sbc"
s1.display()

s2 = Student("Harsh Patel","harshu234@gmail.com",25)
s2.display()


Student.test()
Student.demo()















# Tasks for constructor = productname,price and quantity

# class Product:

#     def __init__(self,pname,price,quantity):
#         self.pname = pname
#         self.price = price
#         self.quantity = quantity

#     def display(self):
#         print(self.pname,self.price,self.quantity)

# p1 = Product("Butter",100,3)
# p1.display()

# p2 = Product("Hair oil",70,1)
# p2.display()