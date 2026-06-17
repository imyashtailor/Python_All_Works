#What is map function in python ?
# it is an built in tool that applies specified function to every item in an iterable(like list,tuple and dictionary)
# return in an iterator and containing the result that is known as map function.

# a = [1,2,3,4,5,6,7]
# k = []

# for i in a:
#     print(i*i)
#     k.append(i)


#map function :- ek ek element par function pass karvanu kam kare
# puri list ke item par operations perform karta he

#using map method :- 
# a = [1,2,3,4,5,6,7]
# k = map(lambda i : i*i,a)
# print(list(k))


# #using length for each element and use map function
# sub = ["java","python","node","php","android"]
# b = map(lambda k : len(k),sub)
# print(list(b))


a = [1,2,3,4,5,6,7]
#OUTPUT :- return the output in boolean value 
k = map(lambda i: i % 2==0,a)
print(list(k))

a = [1,2,3,4,5,6,7]
#OUTPUT :- return the output in value or content
k = filter(lambda i: i % 2==0,a)
print(list(k))