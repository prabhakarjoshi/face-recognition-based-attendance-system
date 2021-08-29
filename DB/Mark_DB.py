import mysql.connector
from datetime import date, datetime

today=f"{datetime.now():%d%m%Y}"
current_time = datetime.now().strftime("%H%M")

def Mark_DB_Fun(myset):                           
    mydb=mysql.connector.connect(host="localhost",
    user="root",
    password="",
    database="face-recognition")
    cursor = mydb.cursor()
    for i in myset:
        query1 = "INSERT INTO `attendance`(`STUDENT_ID`, `TIME`, `DATE`) VALUES ('"+str(i)+"','"+current_time+"','"+today+"')"    
        cursor.execute(query1)
        mydb.commit()

    cursor.close()
    mydb.close()  