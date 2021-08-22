import os
import sys
sys.path.append(os.getcwd()+"\\GUI")

# import Landing_Page_GUI
# from Landing_Page_GUI import Landing_Page_GUI_Fun
from tkinter import *
from tkinter import font 
from PIL import Image,ImageTk

print(sys.path)


def MyImage(str):
    imge=Image.open("Images\\"+str+".png")
    return ImageTk.PhotoImage(imge)  

def Dashboard_UI_Fun():

    def log_out():
        root4.destroy()
        # Landing_Page_GUI_Fun()



    print("dash")
    root4=Tk()
    # root4=Toplevel()
    width= root4.winfo_screenwidth() 
    height= root4.winfo_screenheight()
    print(width)
    root4.geometry("%dx%d" % (width, height))
    root4.configure(bg="#2C394B")
    root4.title("Admin Dashboard")
    root4.resizable(0,1)
    photo=MyImage("Add Student")
    photo1=MyImage("Take Sample")
    photo2=MyImage("Train")
    photo3=MyImage("Log out")
    myFont = font.Font(family='Arial' ,size=20)

    but_add=Button(root4, text='Add Student',image=photo,compound=TOP,font=myFont,activebackground="#2C394B", border=0,bg="#2C394B",fg="#ffffff").place(x=128,y=140)
    but_take_sample=Button(root4, text='Take Sample',image=photo1,compound=TOP,border=0,font=myFont,activebackground="#2C394B",bg="#2C394B",fg="#ffffff",command=Take_Sample_).place(x=458,y=380)
    but_train=Button(root4, text='Train Sample',image=photo2,compound=TOP,border=0,font=myFont,activebackground="#2C394B",bg="#2C394B",fg="#ffffff").place(x=788,y=140)
    but_logout=Button(root4, text='Log Out',image=photo3,compound=TOP,border=0,font=myFont,activebackground="#2C394B",bg="#2C394B",fg="#ffffff",command=log_out).place(x=1118,y=380)

    root4.mainloop()
# Dashboard_UI_Fun()
