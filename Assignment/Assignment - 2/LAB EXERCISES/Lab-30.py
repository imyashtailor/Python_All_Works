#Aim :- Write a Python program that uses a custom iterator to iterate over a list of integers.

def count(n):
    for i in range(n):
        yield i

for num in count(5):
    print(num)