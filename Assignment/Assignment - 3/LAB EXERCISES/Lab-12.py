#Aim :- Write a Python program to demonstrate the use of local and global variables in a class.

id = 100 #Global Variable
class A:

    def test1(self):
        id = 10 #local variable
        # print("local id is calling")

        print("Local Variable = ",id)
        print("Global Varaible = ",globals()['id'])

a = A()
a.test1()