# a = [1,2,3,4,5,6,7]
# k = []

# for i in a:
#     print(i*i)
#     k.append(i)


#map function :- ek ek element par function pass karvanu kam kare

#using map method :- 
a = [1,2,3,4,5,6,7]
k = map(lambda i : i*i,a)
print(list(k))


#using length for each element and use map function
sub = ["java","python","node","php","android"]
b = map(lambda k : len(k),sub)
print(list(b))

