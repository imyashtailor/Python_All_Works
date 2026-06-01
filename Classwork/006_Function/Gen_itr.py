#iterator :- ek ek element ne kadhvu (or find) karva mate use thy.
#defination :- an iterator is an object that allows traverse the all element through collections one by one that
# is known as iterator

# l = [10,20,30,40,50]

# itr = iter(l)

# print(next(itr))
# print(next(itr))
# print(next(itr))
# print("Hello")
# print(next(itr))

#generator :- ek easy way he iterator banana ke liye or iterator object return karta he yeild keyword ke help se 
#using the yeild keyword for making custome generator for iterator

# def test():
#     yield "Hello"
#     yield "Python"

# itr = test()
# print(next(itr))
# print(next(itr))

#looping through karvu hoi to and make karvu hoi to generator no use karvo.
def square(a):
    for i in range(a):
        yield i*i

itr = square(5)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
# print(next(itr))