import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root",
    database="rkce",)
c=mydb.cursor()

c.execute("select * from student")
students=c.fetchall()
for student in students:
    print(student[0]," ",student[1])