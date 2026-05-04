#creating a tuple
# t = (10,20,30,40,50,"ddsd",56.44)
# print(t)
# print(type(t))
# print(len(t))

#another way to create tuple
# a =  tuple((10,20,60,70))
# print(a)

#creating and add element in tuple
#first convert the tuple in list, then append the item in third varaible then converting to tuple and then print.
t = ("Python","Java","Android","Spring_Boot")

# k = list(t)
# k.append("React")
# t = tuple(k)
# print(t)

#Unpack Tuples
# (*a,b,c) = ("Python","Java","Android","Spring_Boot","React")
# print(a)
# print(b)
# print(c)

# print(t*2) double var print thy 

#delete method
# error message :- t is not defined 
# del t
# print(t)

k = [10]
print(type(k))

#how to check type of tuple?
l = (10,)
print(type(l))

#tuples of tuple
#accessing the value from 50
a = ((10,20),(30,40),(50,60))
print(a[2][0])

#concatenations (+)
s1 = (10,40,60,80)
s2 = (20,50,30,70)

print(s1 + s2)

#repetation(*)

print(s1*2)

#membership operator (in, not in)
print(40 in s1)
print(70 not in s1)