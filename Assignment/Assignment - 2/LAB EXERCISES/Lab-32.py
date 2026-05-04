#Aim :- Write a Python program that uses reduce() to find the product of a list of numbers.

from functools import reduce

l = [12,4,23,5,32,2]
def mul(a,b):
    res = a*b
    print(f"{a} X {b} = {res}")
    return res

r = reduce(mul,l)
print("Final Output = ",r)