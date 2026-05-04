#reducer :- single value return (output) kare element mathi
from functools import reduce

#Manual rite
# l = [10,20,30,40,50,60,70,41,58,68]
# def sum(a,b):
#     return a+b

# k=0 #global variable
# for i in l:
#     k = sum(i,k)
# print(k)

#reducer(Automatic) rite
l = [10,20,30,40,50,60,70,41,58,68]
def sum(a,b):
    return a+b

r = reduce(sum,l)
print(r)


# l = [10,20,30,40,50,60,70,41,58,68]

# r = reduce(lambda a,b : a+b,l)

#maximum and minimum find using reduce and lambda
# r = reduce(lambda a,b : a if a>b else b,l)
# r = reduce(lambda a,b : a if a<b else b,l)

# print(r)
