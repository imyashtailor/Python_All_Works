a = int(input("Enter the Number 1 = "))
b = int(input("Enter the Number 2 = "))

choice = "y"
while choice != "n":
    ch = int(input("Enter Choice = "))

    match ch:
        case 1 : print(a+b)
        case 2 : print(a-b)
        case 3 : print(a*b)
        case 4 : print(a/b)
        case _ : print("Invalid Choice")
      
    choice = input("Do you want to continue? y or n = ")