from GUI.Mark_Manually import Mark_Manuallly_Fun
import tkinter
from GUI.Export_UI import Export_UI_Fun
from tkinter import  *
import os
from tkinter.font import Font
from GUI.Export_UI import Export_UI_Fun
from DB.Delete_All import Delete_All_Fun



def Manage_UI_Fun():
    root7=Tk()

    def View_Sample():
        root7.destroy()
        os.startfile("Data")

    def Delete_All_Fun_Helper():
        root7.destroy()
        Delete_All_Fun()
        tkinter.messagebox.showinfo("done","Deleted all attendance")

    def Export_UI_Fun_Helper():
        root7.destroy()
        Export_UI_Fun()
        
            

    root7.geometry("450x350")
    root7.configure(bg="#FFE459")
    root7.title("Manage data")
    root7.resizable(0,0)
    myFont = Font(family='Arial')

    but_mark=Button(root7, text='Mark Manually',font=myFont,activeforeground="#ffffff", activebackground="#FFE459", border=0,bg="#C2F784",fg="#000000",width=20,height=7,command=Mark_Manuallly_Fun).grid(column=0, row=0)
    but_export=Button(root7, text='Export Data',font=myFont, border=0,activebackground="#FFE459",bg="#1E3163",fg="#ffffff",width=20,height=7,command=Export_UI_Fun_Helper).grid(column=0, row=1)
    but_delete=Button(root7, text='Delete Attendance',font=myFont, border=0,activebackground="#FFE459",bg="#1E3163",fg="#ffffff",width=20,height=7,command=Delete_All_Fun_Helper).grid(column=1, row=0)
    but_View=Button(root7, text='View Sample',font=myFont, border=0,activeforeground="#ffffff",activebackground="#FFE459",bg="#C2F784",fg="#000000",width=20,height=7,command=View_Sample).grid(column=1, row=1)
    root7.mainloop()

