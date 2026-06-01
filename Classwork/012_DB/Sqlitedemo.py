import sqlite3

#connection and refer the connection name
con = sqlite3.connect("test.db")

#create a table
# query = "create table students(id int primary key, name varchar(50), email varchar(50))"

#insert the data
# query = "insert into students values(1,'Yash Tailor','yash123@gmail.com')"
# query = "insert into students values(2,'Raj Patel','raj354@gmail.com')"

#update the data
# query = "update students set name = 'Kenil P', email = 'kenil231@gmail.com' where id=2"

#delete data
# query = "Delete from students where id = 2"


#show the data (view data)
query = "select *from students"

#fetchall :- baddha data ne show karava mate terminal ma.
data = con.execute(query).fetchall()
for i in data:
    print(i)



#exceute the query
# con.execute(query)
# con.commit() #insert, update and delete ma commit aapvanu to j data insert thase.