#Naming Conventions
#Name mangling 

# default :- public => Accessible by everywhere
#_ :- protected => within class and subclasses
#__:- private => within the class only
#dir() :-koi pn class no object ma property ketli che te check karva mate dir() no use thy.

class Test:
    id = 10
    _name = "Yash"
    __email = "yash123@gmail.com"

t = Test()
print(dir(t))
print(t.id)
print(t._name)
print(t._Test__email)
