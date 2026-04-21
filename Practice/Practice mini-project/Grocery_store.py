category = ['Vegetable & Foods', 'Dairy', 'Meat', 'Bakery', 'Beverages']

grocery_list = {cat:[] for cat in category}

while True:
    print("------Grocery List--------")
    print("\n1.Add Item")
    print("2.View Item")
    print("3.Update Item")
    print("4.Delete Item")
    print("5.Exit")

    choice = int(input("Enter your choice = "))

    # -------- ADD ITEM --------
    if choice==1:
        for i in range(len(category)):
            print(i+1, category[i])
        
        cat_choice = int(input("Choose Category = "))
        item = input("Enter Item = ")
        
        selected = category[cat_choice-1]
        
        if item in grocery_list[selected]:    
            print("Item already exists!")
        else:
            grocery_list[selected].append(item)
            print("Item added Successfully!")
        
        more = input("Do you want to add more items(yes/no) = ").lower()

        if more!='yes':
            print("Thank you for your time ",end="")
            print("GoodDay!")
            break
        
    # -------- VIEW LIST --------
    elif choice==2:
        if not grocery_list:
            print("Not Found Item")
        else:
            print("Below the Items:")
            for cat in category:
                if grocery_list[cat]:
                    print(f"{cat}:")
                    for j, item in enumerate(grocery_list[cat], start=1):
                        print(f"{j}.{item}")

    # -------- UPDATE LIST --------
    elif choice==3:
        #step-1 show categories
        for i in range(len(category)):
            print(i+1, category[i])
        
        cat_choice = int(input("Choose Category = "))
        selected = category[cat_choice-1]

        #step-2 check if category items
        if not grocery_list[selected]:
            print("Not Item in this category")
        else:
            #show item in this category
            for i, item in enumerate(grocery_list[selected]):
                print(i,item)

                message = int(input("Which number of item do you want to update in list = "))

                if 0<= message < len(grocery_list[selected]):
                    new_item = input("Enter New Item = ")
                    grocery_list[selected][message] = new_item
                    print("Item Updated Successfully!...")
                    print("Updated List:",grocery_list)
                else:
                    print("Invalid index")
    
    # -------- DELETE LIST --------
    elif choice==4:
        #step-1 show categories
        for i in range(len(category)):
            print(i+1, category[i])
        
        cat_choice = int(input("Choose Category = "))
        selected = category[cat_choice-1]

        #step-2 check if category items
        if not grocery_list[selected]:
            print("Not Item in this category")
        else:
            #show item in this category
            for i, item in enumerate(grocery_list[selected]):
                print(i,item)

                message = int(input("Which number of item do you want to Delete in list = "))

                if 0<= message < len(grocery_list[selected]):
                    #remove item
                    remove_item = grocery_list[selected].pop(message)
                    print("Item Deleted Successfully!...")
                    print("Updated List:",grocery_list)
                else:
                    print("Invalid index")
    
    # -------- Final  --------
    elif choice==5:
        print("Thank you for choosing our CLI App ",end="")
        print("Have a good day!...")
