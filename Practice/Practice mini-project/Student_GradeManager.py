students = {}

def add_student():
    try:
        name = input("Enter the Name = ")

        if name in students:
            print("name already exists!..")
            return

        marks = float(input("Enter final percentage = "))

        if marks < 0 and marks > 100:
            print("Marks should be between 0 to 100")
            return
        
        students[name] = marks
        print("Student Added Successfully!...")
        print("\n")
    except Exception as e:
        print(e)

def view_student():
    if not students:
        print("No record found")
        return
    print("\n")    
    print("Student Record")
    for name, marks in students.items():
        print(f"{name} : {marks}")

def search_student():
    name = input("Enter search by student_name = ").strip()

    if name in students:
        print(f"{name}'s marks = {students[name]}")
    else:
        print("Data Not Found")

def Calculate_avg():
    if not students:
        print("Student Not Found")
        return
    
    avg = sum(students.values()) / len(students)
    print(f"Average Marks is {avg:.2f}") 

def find_topper():
    if not students:
        print("Not Found Record")
    
    topper = max(students,key=students.get)
    print(f"Topper is {topper} with {students[topper]} marks")

def delete_student():
    name = input("Enter student name do you want to delete? = ").strip()

    if name in students:
        del students[name]
        print(f"{name} Deleted Successfully!...")
    else:
        print("Not Found Student Record")
    

while True:
    print("========Student Grade Manager=============")
    print("1.Add Students")
    print("2.View Students")
    print("3.Search Students")
    print("4.Calculate Average")
    print("5.Find Topper")
    print("6.Delete Students")
    print("7.Exit")

    choice = int(input("Enter Your choice = "))

    if choice==1:
        add_student()
    elif choice==2:
        view_student()
    elif choice==3:
        search_student()
    elif choice==4:
        Calculate_avg()
    elif choice==5:
        find_topper()
    elif choice==6:
        delete_student()
    elif choice==7:
        print("Good Bye!.. See you next time")
        break