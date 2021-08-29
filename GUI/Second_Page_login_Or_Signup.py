from GUI.Get_The_Password_UI import Get_The_Password_fun
from DB.Login_Validate_db import Login_Validate_fun
from tkinter import *

def Second_Page_login_Or_Signup_fun():
    login=False

    def LoginValidateHelper(arg=None): 
        Login_Validate_fun(login,entry_1.get(),entry_2.get(),entry_3.get(),root1)  
    
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


    label_1 = Label(root1, text="Name :",width=20, font=("bold", 10))
    label_1.place(x=40,y=40)

    entry_1 = Entry(root1)
    entry_1.place(x=200,y=40)

    label_2 = Label(root1, text="Code No. :",width=20,font=("bold", 10))
    label_2.place(x=40,y=80)

    entry_2 = Entry(root1)
    entry_2.place(x=200,y=80)

    label_3 = Label(root1, text="Password :",width=20,font=("bold", 10))
    label_3.place(x=40,y=120)

    entry_3 = Entry(root1,show="*")
    entry_3.place(x=200,y=120)
    

    but_log=Button(root1, text='Log In',width=12,bg='brown',fg='white',command=LoginValidateHelper)
    but_log.place(x=150,y=180)

    but_create=Button(root1, text='Create an account',width=13,bg='brown',fg='white',command=Switching)
    but_create.place(x=5,y=270)
    but_forget=Button(root1, text='Forget Password',width=12,bg='brown',fg='white',command=Get_The_Password_fun)
    but_forget.place(x=300,y=270)
    Switching()
    root1.bind("<Return>",LoginValidateHelper)

    root1.mainloop()