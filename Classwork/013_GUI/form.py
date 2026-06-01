from tkinter import *
import sqlite3

#connection to the database in sqllite
con = sqlite3.connect("form.db")

#creating a form table can store the data
# con.execute("create table auth1(id int primary key, name varchar(20), email varchar(50), password varchar(10))")

root = Tk()
root.geometry("500x500")
root.title("Login Form")
root.configure(bg="#e9f1f7")

#create function
def create():
    name = t1.get()
    email = t2.get()
    password = t3.get()

    con.execute(f"insert into auth1 values('{id}','{name}','{email}','{password}')")
    con.commit()
    print("Data Inserted Successfully!....")

# Header
title = Label(
    root,
    text="LOGIN FORM",
    font=("Arial", 18, "bold"),
    bg="#e9f1f7",
    fg="#2c3e50"
)
title.place(x=170, y=30)

# Username
name = Label(
    root,
    text="Username",
    font=("Arial", 11, "bold"),
    bg="#e9f1f7",
    fg="#34495e"
)
name.place(x=100, y=120)

t1 = Entry(
    root,
    font=("Arial", 11),
    width=28,
    bd=2,
    relief="solid",
    highlightthickness=2,
    highlightbackground="#cfd8dc",
    highlightcolor="#4a90e2",
    bg="white",
    fg="#2c3e50"
)
t1.place(x=200, y=120)

# Email
email = Label(
    root,
    text="Email",
    font=("Arial", 11, "bold"),
    bg="#e9f1f7",
    fg="#34495e"
)
email.place(x=100, y=170)

t2 = Entry(
    root,
    font=("Arial", 11),
    width=28,
    bd=2,
    relief="solid",
    highlightthickness=2,
    highlightbackground="#cfd8dc",
    highlightcolor="#4a90e2",
    bg="white",
    fg="#2c3e50"
)
t2.place(x=200, y=170)

# Password
password = Label(
    root,
    text="Password",
    font=("Arial", 11, "bold"),
    bg="#e9f1f7",
    fg="#34495e"
)
password.place(x=100, y=220)

t3 = Entry(
    root,
    font=("Arial", 11),
    width=28,
    bd=2,
    relief="solid",
    show="*",
    highlightthickness=2,
    highlightbackground="#cfd8dc",
    highlightcolor="#4a90e2",
    bg="white",
    fg="#2c3e50"
)
t3.place(x=200, y=220)

# Submit Button
b = Button(
    root,
    text="SUBMIT",
    font=("Arial", 11, "bold"),
    bg="#2ecc71",
    fg="white",
    activebackground="#27ae60",
    activeforeground="white",
    width=15,
    bd=0,
    cursor="hand2",
    command=create
)
b.place(x=200, y=280)

root.mainloop()