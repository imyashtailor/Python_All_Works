#difference between read() readline() and readlines()

#read() :- old data ne read kare
#readline() :- one by one data ne read kare
#readlines() :- baddha data ne list format ma read kare




#create the file and open and use the write mode

# f = open("test.txt",'w')
# f.write("Hello Python") #single element write karva mate
# f.writelines(["Hello","Python","Hello","Java"]) #multiple senetence lakhva mate
# f.close()

#file_mode append() :- koi bi element or senetence ne add akrva mate
#and previous data erase ni thy aetle use thy.

# f = open("test.txt",'a')
# f.write("Hello Python") #single element write karva mate
# f.writelines(["Hello\n","Tops\n","Hello\n","Bilimora\n"]) #append (insert karva mate koi element ne)
# f.close()

#read the operation (data output ma print thy).

# f = open("test.txt",'r')
# data = f.read()  #read the data (old data ne read karva mate)
# print(data)
# f.close()

# f = open("test.txt",'r')
# while True:
#     data = f.readline()
#     if 'e' in data:
#         print(data)
#     if not data:
#         break
# f.close() 

# f = open("test.txt",'r')
# while True:
#     data = f.readlines()
#     if 'e' in data:
#         print(data)
#     if not data:
#         break
# f.close() 

# with open("test.txt", "r") as f:
#     for line in f:
#         if line.startswith("H"):
#             print(line, end="")


# with open("home.txt",'w') as f:
#     f.write("Hello Something")

# with open("home.txt",'r') as f:
#     print(f.tell())    #kayi jagyaye par cursor che te batave
#     f.seek(5)  #position change kari sakay 
#     data = f.read()
#     print(f.tell()) 
#     print(data)

#r+() :- agar file exist ni hoi to error aave and file exist hoi to ae read and write banne kari dey
# with open("abc.txt",'r+') as f:
#     f.write("Write something")
#     f.seek(0)
#     data = f.read()
#     print(data)

#w+(write and read banne kari day) :- first created a file then write and read in output screen
# with open("abc.txt",'w+') as f:
#     f.write("Write something")
#     f.seek(0)
#     data = f.read()
#     print(data)


#a+(append karva mate multiple var value aave)
# with open("abc.txt",'a+') as f:
#     f.write("Write something")
#     f.seek(0)
#     data = f.read()
#     print(data)


#rb (binary file or images access karva mate)
# with open("abc.png","rb") as f:
#     data = f.read()
#     print(data)   

#json file

# import json
# d = {"name" : "yash","email":"yash123@gmail.com","age":25,"City":"Bilimora"}
# with open("data.json",'w') as f:
#     json.dump(d,f)

#json file ne read karva mate json.load() function no use karvo.
# with open("data.json","r") as f:
#     data = json.load(f)
#     print(data)