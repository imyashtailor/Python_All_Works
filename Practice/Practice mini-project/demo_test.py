import sqlite3

con = sqlite3.connect("hello.db")

#query = "create table stuinfo(id int primary key, name varchar(50), age varchar(10), email varchar(50), city varchar(20))"

query = "insert into stuinfo values(2,'Krunal Rathod',22,'krunal134@gmail.com','Bardoli')"

print("Record Inserted Successfully!....")
con.execute(query)
con.commit()