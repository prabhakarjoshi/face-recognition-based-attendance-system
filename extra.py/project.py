from tkinter import *
from tkinter import font 
import tkinter.messagebox
from PIL import Image,ImageTk
import mysql.connector


mydb=mysql.connector.connect(host="localhost",
user="root",
password="",
database="face-recognition")
cursor = mydb.cursor()

def MyImage(str):
    imge=Image.open(str+".png")
    return ImageTk.PhotoImage(imge)
def Verifying(login,name,mobile,passw):
    
    if login:
        # check data
        print("login")
        # display all records
        # table = cursor.fetchall()
  
        # describe table
        # print('\n Table Description:')
        # for attr in table:
        #     print(attr)    

    else:
       
        
        # assign data query
        # query1 = "INSERT INTO `login` (`username`, `password`, `mobile number`) VALUES ('"+name.get()+"', '"+passw.get()+"', '"+mobile.get()+"');"
        query1 = "INSERT INTO `login` (`username`, `password`, `mobile number`) VALUES ('a', 'b', 'c')"
  
        # executing cursor
        cursor.execute(query1)
  
    

    
def createLoginWindow():
    login=False
    def VerifyingHelper():  
        Verifying(login,name,mobile,passw)  
    def Switching(arg=None):
        nonlocal login
        print(login)
        if (login):
            label_2.place(x=40,y=80)
            entry_2.place(x=200,y=80)
            label_1.place(x=40,y=40)
            entry_1.place(x=200,y=40)
            but_forget.place_forget()
            but_log.configure(text="Sign Up")
            but_create.configure(text="Have an account?")
            login=False    
        else:
            label_2.place_forget()
            entry_2.place_forget()
            label_1.place(x=40,y=60)
            entry_1.place(x=200,y=60)

            but_create.configure(text="Create an account")
            but_log.configure(text="Log in")
            but_forget.place(x=300,y=270)
            login=True

        
        
    root1=Tk()
    root1.geometry('400x300')
    root1.title("Login or signup")
    root1.resizable(0,0)
    name=StringVar()
    mobile=StringVar()
    passw=StringVar()

    label_1 = Label(root1, text="Name :",width=20, font=("bold", 10))
    label_1.place(x=40,y=40)

    entry_1 = Entry(root1,textvar=name)
    entry_1.place(x=200,y=40)


    label_2 = Label(root1, text="Mobile No. :",width=20,font=("bold", 10))
    label_2.place(x=40,y=80)

    entry_2 = Entry(root1,textvar=mobile)
    entry_2.place(x=200,y=80)

    label_3 = Label(root1, text="Password :",width=20,font=("bold", 10))
    label_3.place(x=40,y=120)

    entry_3 = Entry(root1,textvar=passw,show="*")
    entry_3.place(x=200,y=120)
    

    but_log=Button(root1, text='Log In',width=12,bg='brown',fg='white',command=VerifyingHelper)
    but_log.place(x=150,y=180)
    # root1.bind("<Return>",HideWidget)

    but_create=Button(root1, text='Create an account',width=13,bg='brown',fg='white',command=Switching)
    but_create.place(x=5,y=270)
    but_forget=Button(root1, text='Forget Password',width=12,bg='brown',fg='white')
    but_forget.place(x=300,y=270)
    Switching()

    root1.mainloop()



root = Tk()
root.geometry('600x500')
root.configure(bg="#6B7AA1")
root.title("Attendence Management System")
root.resizable(0,0)

label_design = Label(root,bg="#C1CFC0",width=50,height=40)
label_design.place(x=300,y=0)

myFont = font.Font(family='Courier', size=20, weight='bold')
photo=MyImage("admin")
but_admin_login=Button(root, text='ADMIN',image=photo, width=200,height=300,compound=TOP,font=myFont,bg="#C1CFC0",command=createLoginWindow).place(x=95,y=90)
photo1=MyImage("user")
but_user=Button(root, text='USER',image=photo1,height=300,compound=TOP,font=myFont, width=200,bg="#6B7AA1").place(x=300,y=90)



root.mainloop()
