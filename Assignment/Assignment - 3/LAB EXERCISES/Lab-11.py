#Aim :- Write a Python program to create a class and access its properties using an object.

class car:
    name = "Vitara_brezza"
    color = "Black"
    brand = "Suzuki"

    def display(self):
        print(self.name,self.color,self.brand)

c1 = car()
c1.display()