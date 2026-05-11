#try :- problemtic error try ma aavse
#except :- error handle thy
#else:- try ma koi error ni hoi and try execute thy to j else part chale
#finally :- always executable rey


print("Program Started")
try:
    a=10
    b = a/0
    print(b)
except Exception as e:
    print(e)
else:
    print("Something")
finally:
    print("Always Executable")
print("Program Ended")