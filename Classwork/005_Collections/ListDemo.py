# l = [10,20,30,40,"abc",False,45.66]
# print(l)
# print(type(l))
# print(l[1])

# #creating a constructor
# l = list((10,20,30,40,50))
# print(l)

# access list item :
# l = [10,20,30,40,50,60]
# print(l[1])
# print(l[1:5])
# print(l[-1])
# print(l[-4:-1])
# print(l[::-1])

#change the list
# l = [10,20,30,40,50,60]
# l[0] = 100
# l.insert(1,300)
# l.append(200)
# l[:5] = [34,56,78,54,45,78,78,89]
# print(l)

#extend the list
# a = [10,20,30]
# b = [40,50,60]
# a.extend(b)
# print(a)

#remove the list
# l = [10,20,30,40,50,60]
# l.remove(30)
# l.pop(3)
# l.clear()
# del l
# print(l)

#accessing element loop through:-
# for i in l:
#     print(i)

# for i in range(len(l)):
#     print(l[i])

# i=0

# while i<len(l):
#     print(l[i])
#     i+=1

# koi bi sepcific string or word ne find karva and tene print karva mate aakhi string ne 
#list comprehension
# s = ['python','java','android','php','react']
# l=[]

# for i in s:
#     if "a" in i:
#         l.append(i)
# print(l)

#list comprehension
# l = [i for i in s if "a" in i]
# print(l)

# k = [i for i in s if i.startswith('p')]
# print(k)

# l = [10,20,40,80]
# k = [i for i in l if i%2!=0]
# print(k)

# my_list=[1,2,3]
# # list2 =[4,5,6]
# my_list[1]=5
# print(my_list)
#sort method 

# s = ['Python','Android','Java','SQL']
# s.sort()
# s.sort(reverse=True)
# s.reverse()
# print(s)

# k = sorted(s)
# print(k)

#copy the string
# s = ['Python','Android','Java','SQL']
# k = s
# k = s.copy()
# k = list(s)
# k = s[:]

# k.append(5000)
# print(k)
# print(s)

#index() method :- used to find the position (index) of a value inside a list
# a = [10,20,30]
# print(a.index(20))

#count :- list ni under same value jetli var hoi tene count kare
a = [10,20,30,40,50,30,30]
print(a.count(30))

# print("abc".count(3))

s=[10,50,50]
l = ["abc" for i in s if i==50]
print(l)






