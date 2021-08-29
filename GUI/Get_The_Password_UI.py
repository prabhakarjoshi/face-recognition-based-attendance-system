from DB.Get_Password_db import Get_Password_db_fun
from tkinter import *
import tkinter.messagebox


def Get_The_Password_fun():

    def Get_Password_db_fun_helper():
        str=Get_Password_db_fun(entry_1.get(),entry_2.get())
        root3.destroy()
        tkinter.messagebox.showinfo("Password","Your Password is '"+str+"'")
        # root3.destroy()
    
    root3=Tk()
    root3.geometry('400x300')
    root3.title("Forget Password")
    root3.resizable(0,0)

    label_1 = Label(root3, text="Name :",width=20, font=("bold", 10))
    label_1.place(x=40,y=40)

    entry_1 = Entry(root3)
    entry_1.place(x=200,y=40)

    label_2 = Label(root3, text="Code No. :",width=20,font=("bold", 10))
    label_2.place(x=40,y=80)

    entry_2 = Entry(root3)
    entry_2.place(x=200,y=80)
    
    but_Get=Button(root3, text='Get Password',width=12,bg='brown',fg='white',command=Get_Password_db_fun_helper)
    but_Get.place(x=150,y=180)
    root3.mainloop()