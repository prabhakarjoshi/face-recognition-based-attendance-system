
import mysql.connector

def Get_Name_DB_Fun(id):
    nid = "% s" % id                                
    mydb=mysql.connector.connect(host="localhost",
    user="root",
    password="",
    database="face-recognition")
    cursor = mydb.cursor()
    query1 = "SELECT NAME FROM students WHERE `STUDENT_ID`='"+ nid+"'"
    cursor.execute(query1)
    for row in cursor:
        a=(row[0])
    cursor.close()
    mydb.close()     
    return a