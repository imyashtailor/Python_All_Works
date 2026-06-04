#Aim :- Write a Python program to connect to an SQLite3 database, create a table, insert data, and fetch data. 

from tkinter import *
import sqlite3

#conncetin to the sqlite3
con = sqlite3.connect("reg.db")

# con.execute("create table register(name varchar(20), course varchar(30), sem varchar(20), form varchar(10), contact varchar(10), email varchar(40), address varchar(20))")

#get the data
def create():
    name = t1.get()
    course = t2.get()
    sem = t3.get()
    form = t4.get()
    contact = t5.get()
    email = t6.get()
    address = t7.get()

    #insert the data
    con.execute(f"insert into register values('{name}','{course}','{sem}','{form}','{contact}','{email}','{address}')")
    con.commit()

    print("Registration Successfully!....")


root = Tk()
root.geometry("500x500")
root.title("Simple App")

# Heading
title = Label(
    root,
    text="Registration Form",
    font=("Arial", 18, "bold"),
    bg="#f0f4f8",
    fg="#2c3e50"
)
title.pack(pady=20)

name = Label(root,text="Name")
name.place(x=100,y=100)

course = Label(root,text="Course")
course.place(x=100,y=150)

sem = Label(root,text="Semester")
sem.place(x=100,y=200)

form = Label(root,text="Form_No.")
form.place(x=100,y=250)

contact = Label(root,text="Contact_No.")
contact.place(x=100,y=300)

email = Label(root,text="Email_id")
email.place(x=100,y=350)

address = Label(root,text="Address")
address.place(x=100,y=400)

t1 = Entry(root)
t1.place(x=200,y=100)

t2 = Entry(root)
t2.place(x=200,y=150)

t3 = Entry(root)
t3.place(x=200,y=200)

t4 = Entry(root)
t4.place(x=200,y=250)

t5 = Entry(root)
t5.place(x=200,y=300)

t6 = Entry(root)
t6.place(x=200,y=350)

t7 = Entry(root)
t7.place(x=200,y=400)

b = Button(root,text="Register",width=17,command=create)
b.place(x=200,y=430)

root.mainloop()