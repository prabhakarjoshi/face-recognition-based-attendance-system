import mysql.connector

def pr():
    print("hjk")
mydb=mysql.connector.connect(host="localhost",
user="root",
password="",
database="face-recognition")
cursor = mydb.cursor()
query1 = "INSERT INTO `login` (`username`, `password`, `mobile number`) VALUES ('aa', 'ba', 'ca')"
  
# executing cursor
cursor.execute(query1)
  
# display all records
# table = cursor.fetchall()
  
# describe table
# print('\n Table Description:')
# for attr in table:
# #     print(attr)
# query2 = "select * from login"
  
# # executing cursor
# cursor.execute(query2)
  
# # display all records
# table = cursor.fetchall()
  
# # fetch all columns
# print('\n Table Data:')
# for row in table:
#     print(row[0], end=" ")
#     print(row[1], end="\n ")

cursor.execute("commit")    

cursor.close()
  
# closing connection object
mydb.close()