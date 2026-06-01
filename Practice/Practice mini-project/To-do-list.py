from tkinter import *

# =======Functions=======
def add_task():
    task = t1.get()
    if task != "":
        lb.insert(END,task)
        t1.delete(0,END)


root = Tk()
root.geometry("500x500")
root.title("To-Do List")
root.config(bg="#f2f2f2")

# Title label
title = Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="#f2f2f2", fg="#333")
title.pack(pady=10)

# Entry box
t1 = Entry(root, font=("Arial", 12), width=25, bd=2, relief=GROOVE)
t1.place(x=120, y=70)

# Button styling helper
btn_style = {
    "font": ("Arial", 11, "bold"),
    "width": 12,
    "bd": 0,
    "relief": FLAT,
    "cursor": "hand2"
}

b1 = Button(root, text="Add Task", bg="#4CAF50", fg="white", **btn_style,command=add_task)
b1.place(x=180, y=120)

b2 = Button(root, text="Delete Task", bg="#f44336", fg="white", **btn_style,command=Delete_task)
b2.place(x=180, y=170)

b3 = Button(root, text="View Task", bg="#2196F3", fg="white", **btn_style,command=View_task)
b3.place(x=180, y=220)

# Listbox with styling
lb = Listbox(
    root,
    width=40,
    height=15,
    font=("Arial", 12),
    bg="white",
    fg="#333",
    bd=2,
    relief=GROOVE,
    selectbackground="#ddd",
    selectforeground="#000"
)
lb.place(x=80, y=280)

root.mainloop()