# s = {10,20,30,40,50,50}
# s.clear()
# print(s)
# for i in s:
#     print(i)

#add the item in set
# s.add(77)
# print(s)

#copy the value from set
# s.copy()
# print(s)

# s.update[(78,89,54)]
# print(s)

#remove the item or value direct in set
#ama value ni hoi to error aave 
# s.remove(77)
# print(s)

#discard :- ae bi same remove jevu j kam kare but aema
#ama program continue rey error ni aave
# s.discard(400)
# print(s)

#pop():- random value delete kari dey set mathi
# s.pop()
# print(s)


# my_set = {10,30,50,70}
# print(my_set) #generate a random number

a = {10,20,30,40,True,0}
b = {30,40,50,60,1,False}

#Union Method - |  => data combine kare but same value return ni kare
# a.update(b)      => add all elements of B into A (no duplicates) --- Update()
# print(a)
# k = a.union(b) => => everyone from both groups, without repeating names. --- Union()
# print(k)


#|(union) symbol method
# c = a | b
# print(c)

#Intersection Method - &  => je data common hoi te aave 
# a.intersection_update(b)
# print(a)
# k = a.intersection(b)
# print(a)

# &(Intersection) Symbol Method - 

#difference Method - - => je data a ma che but b ma nathi and b ma je che te a ma nathi
# a.difference_update(b)
# print(a)
# k = a.difference(b)
# print(k)

#symmetric difference - ^ => common value ni hoi te symmetric kevay
# a.symmetric_difference_update(b)
# print(a)
# k = a.symmetric_difference(b)
# print(k)

#issubest, issuperset and isdisjoint
a = {100,200}
b = {10,20,30}

print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b))

#frozenset method
f = frozenset({10,20,30,40})
print(type(f))
print(f)