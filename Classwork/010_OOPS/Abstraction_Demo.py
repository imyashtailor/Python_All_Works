#Abstraction :- hides the certain details and only show essential information that is known as Abstraction
#Abstraction ma object nai bane , but aene aapde bija class ma object banavi sakiye and call kari sakiye
#Abs ne call karaviye to error aavse


from abc import ABC,abstractmethod

class Abs(ABC):
    @abstractmethod
    def test(self):
        pass

class AbsImpl(Abs):

    def test(self):
        print("Test Calling")

# a = Abs() #error provide because abstact class no object ni bane
k = AbsImpl()
k.test()