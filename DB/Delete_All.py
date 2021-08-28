import mysql.connector

def Delete_All_Fun():
    mydb=mysql.connector.connect(host="localhost",
    user="root",
    password="",
    database="face-recognition")
    cursor = mydb.cursor()
    query1 = 'DELETE FROM `attendance`'    
    cursor.execute(query1)
    cursor.close()
    mydb.close()     