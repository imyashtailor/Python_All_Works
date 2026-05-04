#dictonary ma khali list and set ni chale baki baddhi data type ni chale
#dictonary is mutable and changble
#dictonary are ordered after python version 3.7 , before dictionary is unordered.

# person = {
#     "name" : "yash",
#     "email" : "yash123@gmail.com",
#     "age" : 25,
#     "city" : "Bilimora",
#     "lang" : ["Gujarati","English","Hindi"],
#     123 : "abc",
#     True : "bool",
#     (10,20,30) : "dfd",
#     # [10,20,30] : "dfuihdw"
# }

# print(person)

#other way to create a dictionary
# d = dict(name="abc",email="tailory123@gmail.com")
# print(d)

# cn = {
#     "India" : "IN",
#     "USA" : "US",
#     "Canada" : "CAN",
#     "Australia" : "AUS"
# }

# print(cn)

# print(cn.get("India1")) #meaning => suppose dictionary ni under koi key exist ni hase to none print thase
# print(cn['India1']) #meaning => suppose dictionary ni under koi key exist ni hase to error aapse.
# print("Hello")

# print(cn.keys()) #only key return karse dictionary mathi
# print(cn.values()) #only values return karse dictionary mathi
# print(cn.items()) #key-value pair ma data aavse (list ni under tuple)
# print(cn)

#looping through
# for i,j in cn.items():  #access the dictionary
#     print(i,j)


# cn['India'] = 'abc' #update the only one dictionary key and value
# cn.update({"abc":"xyz","India":"k"}) #update the multiple dictionary value thy
# print(cn)

# cn.pop("India") #key thi value delete thy.
# cn.popitem() #last key and value delete thy.
# cn.clear() #dictionary ni under key and value delete thy only dictionary {} bache
# del cn
# print(cn)


#copy method
# print(cn)
# k = cn.copy() #aa method ma tame k ne change karo to cn na data pn change ni thy bz original che.
# k = cn #jyare ama tame change karo to cn ma pn change thy jay
# k.update({'A':'x'})
# print(k)
# print(cn)

#nested dictionary method

student = {
    "name":"yash",
    "email":"yash345@gmail.com",
    #nested dictionary
    "marks" : {
        "Python" : 50,
        "Java" : 68,
        "PHP" : 89
    }
}

# for i,j in student['marks'].items(): #marks na data ne get karva mate key value pair ma (nested dictionary ma)
#     print(i,j)

# print(student['marks']['Python']) #koi particulary one data na record ne get or return karva mate


#baddha na keys ma common value assign karva mate
# x = ('key1', 'key2', 'key3')
# y=0

# thisdict = dict.fromkeys(x,y)

# print(thisdict)

#zip method :- combine kare and type vise joytu hoi te format ma aave (e.g. list, tuple)
# x = ("k1","k2","k3")
# y = (10,20,30)

# d = zip(x,y)
# print(dict(d))


#setdeafult method :- ama key exist hase to change thase ni thase
k = {"a":1,"b":2}
# k.setdefault("b",3)

#simple add method
k['b'] = 3 # and add karsu to change thy jase 
print(k)






