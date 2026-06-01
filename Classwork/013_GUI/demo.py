from tkinter import *
import sqlite3

#connection of establishes
con = sqlite3.connect("demo.db")

#creating a table
# con.execute("create table login(name varchar(50), email varchar(50), contact varchar(10))")

def create():
    name = t1.get()
    email = t2.get()
    contact = t3.get()

    con.execute(f"insert into login values('{name}','{email}','{contact}')")
    con.commit()
    print("Added details successfully")


root = Tk() #refrence of the root => program starting sentence 
root.geometry("500x500") # tkinter window size leva mate (tamne ketli joye ae according)
root.title("My App")



#Tkinter Library
#pack() :- left, right, top and bottom
#grid() :- row,column
#place() :- x and y axis
#entry :- textbox mate use thy

#pack section :-
# b1 = Button(root,text="LEFT")
# b1.pack(side=LEFT)

# b2 = Button(root,text="RIGHT")
# b2.pack(side=RIGHT)

# b3 = Button(root,text="TOP")
# b3.pack(side=TOP)

# b4 = Button(root,text="BOTTOM")
# b4.pack(side=BOTTOM)

#Grid Section
# name = Label(root,text="Username")
# name.grid(row=1,column=1)

# email = Label(root,text="Email")
# email.grid(row=2,column=1)

# contact = Label(root,text="Phone")
# contact.grid(row=3,column=1)

# t1 = Entry(root)
# t1.grid(row=1,column=2)

# t2 = Entry(root)
# t2.grid(row=2,column=2)

# t3 = Entry(root)
# t3.grid(row=3,column=2)

# b = Button(root,text="Click Me")
# b.grid(row=4,column=2)

# place section :-
name = Label(root,text="Username")
name.place(x=100,y=100)

email = Label(root,text="Email")
email.place(x=100,y=150)

contact = Label(root,text="Phone")
contact.place(x=100,y=200)

t1 = Entry(root)
t1.place(x=200,y=100)

t2 = Entry(root)
t2.place(x=200,y=150)

t3 = Entry(root)
t3.place(x=200,y=200)

b = Button(root,text="submit",width=17,command=create)
b.place(x=200,y=230)

root.mainloop() #program end sentence