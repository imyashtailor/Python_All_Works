#creating local and global scope
print("========create a local and global scope =======")
a = 10 #global scope
def test():
    #local scope
    a = 20
    print(a)

print(a)
test()
print(a)

# print("\n")
print("========Local scope to global scope use global keyword========")
#local che aene mare global karva mate :-
a = 10 #global scope
def test():
    #local scope
    #global keyword use
    global a
    a = 20
    print(a)

print(a)
test()
print(a)
