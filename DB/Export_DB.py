import mysql.connector
from tkinter import filedialog
import pandas as pd

def Export_DB_Fun(course,sec):
    mydb=mysql.connector.connect(host="localhost",
    user="root",
    password="",
    database="face-recognition")
    cursor = mydb.cursor()
    query1 = 'SELECT TIME,DATE,NAME, ROLL_NO, COURSE, SECTION FROM `attendance` a JOIN `students` s ON  s.STUDENT_ID =a.STUDENT_ID AND s.COURSE="'+course+'" AND s.SECTION="'+sec+'"'    
    cursor.execute(query1)
    x=cursor.fetchall()  
    df = pd.DataFrame(x,columns=pd.Index(['TIME','DATE','NAME','ROLL NO','COURSE','SECTION']))
    df.head() 
    name=filedialog.askopenfilename()    
    df.to_excel(name)
    cursor.close()
    mydb.close()     
# Export_DB_Fun("B-Tech","I")