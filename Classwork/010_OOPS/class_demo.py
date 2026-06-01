#class :- class is a collection of variable and functions
#class is an blueprint
#class is collection of where we can define a varibale and functions
#class is an collection of data member and function memeber

#obejct :- object is an instance of the class
#self = class na property ne refer kare
#self.age => particular ek j data ne refer kare.
#and same name nu function banavo and call karo aene to ae latest vadu je create kariyu hase te print karse.

# class Pen:
#     price = 10
#     color = "Blue"
#     company = "DOMS"

#     def to_write(self):
#         print(self.price,self.color,self.company)

# p1 = Pen()
# p1.price=50
# p1.to_write()

# p2 = Pen()
# p2.color="Red"
# p2.to_write()


#Task :- #name,email,contact levu and class create karvu
class Student:
    name = "yash"
    email = "tailory123@gmail.com"
    contact = 9173828868

    def display(self):
        print(self.name,self.email,self.contact)
    
    # def display(self):
    #     print(self.email)

s1 = Student()
# s1.name = "raj"
s1.display()
