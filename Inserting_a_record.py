import sqlite3

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123"
)
mycursor = mydb.cursor()
mycursor.execute("create database newdatabase")
mycursor.execute("use newdatabase")
mycursor.execute("create table student1(name varchar(30) )")
mycursor.execute("create table student2(name varchar(30),address varchar(50),city varchar(70))")
sql= "INSERT INTO student2 (name , address , city ) VALUES (%s,%s,%s)"
val=("RIta","delhi","UP")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted")
mydb.close()
