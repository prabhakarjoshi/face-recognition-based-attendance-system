from os import error
import tkinter.messagebox
import mysql.connector
from Data_Processing.Take_Sample import Take_Sample_Fun

def Add_New_Student_Fun(root5,name,sec,id,roll,course):
    root5.destroy()
    try:
        mydb=mysql.connector.connect(host="localhost",
        user="root",
        password="",
        database="face-recognition")
        cursor = mydb.cursor()
        if not mydb.is_connected:
            tkinter.messagebox.showinfo("Error while connecting to the database!")
        else:
            query1 = "INSERT INTO `students` (`NAME`, `COURSE`, `SECTION`, `ROLL NO`, `STUDENT ID`) VALUES ('"+name+"', '"+course+"', '"+sec+"', '"+roll+"', '"+id+"')"
            cursor.execute(query1)
            cursor.execute("commit")
            Take_Sample_Fun(id)
            
            
            cursor.close()
            mydb.close()
    except error as e:
        print(e)
    


