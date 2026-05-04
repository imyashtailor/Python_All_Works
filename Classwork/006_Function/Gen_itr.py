#iterator :- ek ek element ne kadhvu (or find) karva mate use thy.

# l = [10,20,30,40,50]

# itr = iter(l)

# print(next(itr))
# print(next(itr))
# print(next(itr))
# print("Hello")
# print(next(itr))

#generator :- custome iterator banavu hoi to potanu.
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