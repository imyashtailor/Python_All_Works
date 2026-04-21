category = ['Vegetable & Foods','Dairy','Meat','Bakery','Beverages']
grocery_list = []

while True:
    print("----------Grocery List-------------")
    print("\n1.Vegetables & Foods")
    print("2.Dairy")
    print("3.Meat")
    print("4.Bakery")
    print("5.Beverages")

    choice = int("Enter Category Choice = ")
    for i in category:
        if not i:
            print("Invalid Choice")
        if choice==i:
            match i:
                case 1:
                    print("------Insert Item--------")
                    item = input("Enter Insert New Item = ")
                    grocery_list.insert(item)
                    grocery_list.append(item)
                    print("Item Added Successfully!...")
                    break
                case 2:
                    print("----View Item List------")
                    if not grocery_list:
                        print("Not Found the item")
                    else:
                        print("----Your List Below----")
                        for j,l in enumerate(grocery_list,start=1):
                            print(f"{j}.{t}")