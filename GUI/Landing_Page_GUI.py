from GUI.Second_Page_login_Or_Signup import Second_Page_login_Or_Signup_fun
from Data_Processing.Take_Attendence import Take_Attendence_Fun
from tkinter import *
from tkinter import font 
from PIL import Image,ImageTk

# from Take_Attendence import Take_Attenedence_Fun


def MyImage(str):
    imge=Image.open("Images\\"+str+".png")
    return ImageTk.PhotoImage(imge)  


def Landing_Page_GUI_Fun():
    root = Tk()

    def Second_Page_login_Or_Signup_fun_helper():
        root.destroy()
        Second_Page_login_Or_Signup_fun()    
  

    
    root.geometry('600x500')
    root.configure(bg="#6B7AA1")
    root.title("Attendence Management System")
    root.resizable(0,0)

    label_design = Label(root,bg="#C1CFC0",width=50,height=40)
    label_design.place(x=300,y=0)

    myFont = font.Font(family='Courier', size=20, weight='bold')
    photo=MyImage("admin")
    but_admin_login=Button(root, text='ADMIN',image=photo, width=200,height=300,compound=TOP,font=myFont,bg="#C1CFC0",command=Second_Page_login_Or_Signup_fun_helper,border=0).place(x=95,y=90)
    photo1=MyImage("user")
    but_user=Button(root, text='USER',image=photo1,height=300,compound=TOP,font=myFont, width=200,bg="#6B7AA1",command=Take_Attendence_Fun).place(x=300,y=90)



    root.mainloop()