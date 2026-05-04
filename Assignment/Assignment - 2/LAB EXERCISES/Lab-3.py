#Aim:- Write a Python program to create a list of multiple data type elements.

my_list1 = [10,20.5,"num",4j+5,[1,2,3],(6,7,8),True]

print("\nElements with their data types below")
for i in my_list1:
    print(i,"->",type(i))