from os import error
from tkinter import *
import tkinter.messagebox
import mysql.connector
from GUI.Dashboard_UI import Dashboard_UI_Fun


def Login_Validate_fun(login,name,code,passw,root1):
    try:
        mydb=mysql.connector.connect(host="localhost",
        user="root",
        password="",
        database="face-recognition")
        cursor = mydb.cursor(buffered=True)
        if not mydb.is_connected:
            tkinter.messagebox.showinfo("Error while connecting to the database!")
        else:
            if login:
                # for logging in
                query1 = "SELECT `password` FROM `login` WHERE username='"+name+"'"
                cursor.execute(query1)
                
                for row in cursor:
                    if row[0]==passw:
                        root1.destroy()
                        Dashboard_UI_Fun()
                        break   

                cursor.close()
                mydb.close()
              
            else:
            # for signing in
                query1 = "INSERT INTO `login` (`username`, `password`, `Code number`) VALUES ('"+name+"', '"+passw+"', '"+code+"')"
                cursor.execute(query1)
                cursor.execute("commit")   
                cursor.close()
                mydb.close()
                root1.destroy()
                Dashboard_UI_Fun()
    except error as E:
        print(E)