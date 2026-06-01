#Encapsulation :- wrapping the all information into one container that is known as Encapsulation 
#there are two methods to create and access the object
#Getter and setter
#get() and set()

class Student:

    __id = 10
    __name = "yash"

    def set_id(self,id):
        self.__id = id
    
    def get_id(self):
        return self.__id
    
    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name
    
st = Student()
st.set_id(20)
#change the name
st.set_name("Harsh")
print(st.get_id())
print(st.get_name())
