#filter function :- it is a built in python tool used to extract element from an itreble (like tuple,list) that specify condition.

# a = [1,2,3,4,5,6,7,8,9]
# k = []

# #normal method :-

# def checkodd(a):
#     if a % 2!=0:
#         return a

# for i in a:
#     j = checkodd(i)
#     if j is not None:
#         k.append(j)

# print(k)


#using filter-method
a = [1,2,3,4,5,6,7,8,9,10]
def checkodd(a):
    if a % 2 !=0:
        return a

k = filter(lambda i : i%2!=0,a)
print(list(k))

#practical use 
# sub = ["java","python","node","php","android"]

# k = filter(lambda ele : "a" in ele,sub)
# print(list(k))

# k = filter(lambda ele : ele.startswith("p"),sub)
# print(list(k))