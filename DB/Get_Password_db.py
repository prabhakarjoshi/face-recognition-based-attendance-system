import tkinter.messagebox
import mysql.connector

def Get_Password_db_fun(name,code):
    mydb=mysql.connector.connect(host="localhost",
    user="root",
    password="",
    database="face-recognition")
    cursor = mydb.cursor()
    if not mydb.is_connected:
        tkinter.messagebox.showinfo("Error while connecting to the database!")
    else:
        query1 = "SELECT `password` FROM `login` WHERE  `username`='"+name+"' AND `Code Number`='"+code+"'"
        cursor.execute(query1)
        for row in cursor:
            str=row[0] 
        # str=cursor.fetchone
        # print(str)
        cursor.close()
        mydb.close()