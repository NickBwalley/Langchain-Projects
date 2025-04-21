import sqlite3

## connect to sqllite
connection=sqlite3.connect("student.db")

##create a cursor object to insert record,create table
cursor=connection.cursor()

## create the table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
GRADE VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

## Insert some more records
cursor.execute('''Insert Into STUDENT values('Nick','Data Science','A',95)''')
cursor.execute('''Insert Into STUDENT values('Lesley','Business Intelligence','B',69)''')
cursor.execute('''Insert Into STUDENT values('Kingsley','OOP','C',59)''')
cursor.execute('''Insert Into STUDENT values('Josh','DEVOPS','A',81)''')
cursor.execute('''Insert Into STUDENT values('Aisha','DEVOPS','A',89)''')

## Display all the records
print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()
