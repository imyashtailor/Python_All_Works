import mysql.connector as sql

#conncetion in sql with python

con = sql.connect(
    host="localhost",
    port = 3306,
    user="root",
    password="yash16112001#",
    database = "mydb1"
)
# print("Successfully Connected!...")

cursor = con.cursor()

#database created
# cursor.execute("create database mydb1")

#creating a table
# cursor.execute("create table employee(id int primary key, name varchar(50), department varchar(50), salary int)")

#insert the data
#single value inserted
# cursor.execute("insert into employee values(101,'Yash Tailor','CSE','15000')")

#multiple value inserted data

#Insert Section Part
# q = "insert into employee values(%s,%s,%s,%s)"
# # v = (103,'Ankit Patel','Finance','20000')

# data = [
#     (104,'Ankit Patel','Finance','20000'),
#     (105,'hello Patel','Finance','20000'),
#     (106,'Ankit Patel','Finance','20000')
# ]
# cursor.executemany(q,data)
# con.commit()
# print("Record Inserted Successfully!...")

#Update Section Part :-
# q = "update employee set name = %s, department = %s, salary = %s where id=%s"

# data = [
#     ('Sahil Patel','Marketing','22000',104),
#     ('Gopal Bahvashkar','Developer','30000',105),
#     ('Mohit Parekh','Frontend','25000',106)
# ]
# cursor.executemany(q,data)
# con.commit()
# print("Record Updated Successfully!...")

#Delete Section part :-
# q = "Delete from employee where id = %s"

# data = [
#     (105,),
#     (106,)
# ]
# cursor.executemany(q,data)
# con.commit()
# print('Record Deleted Successfully!....')


#View Data Section:-

q = "select *from employee"
cursor.execute(q)
data = cursor.fetchall()
for i in data:
    print(i)

#only mane limited data joye to
# data = cursor.fetchmany(2)
# print(data)