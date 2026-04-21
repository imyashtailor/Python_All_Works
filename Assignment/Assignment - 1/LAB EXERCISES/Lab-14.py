#Aim :- Write a Python program to find a specific string in the list using a simple for loop and if condition.

List2 = ['Red','Green','Blue','Violet','Purple','Yellow']

search = 'Red'
# search = 'black'

found = False

for i in range(len(List2)):
    if List2[i]==search:
        found = True
        break

if found:
    print("String is Found!..")
else:
    print("String is not Found!..")