#Aim :- Write a Python program to separate keys and values from a dictionary using keys() and values() methods..

student = {
    "name" : "yash",
    "email" : "yash123@gmail.com",
    "contact" : 123456,
    "Address" : "102 street, Bilimora",
    "City" : "Bilimora",
    "Hobby" : "Cricket"
}

keys = student.keys()
values = student.values()

print("Keys:",list(keys))
print("Values:",list(values))

