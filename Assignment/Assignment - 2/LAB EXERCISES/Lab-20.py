#Aim :- Write a Python program to merge two lists into one dictionary using a loop.

my_dict = ["Python","Java","Android","React"]
value = [1,2,3,4]

message = {}

for i in range(len(my_dict)):
    message[my_dict[i]] = value[i]

print(message)
    