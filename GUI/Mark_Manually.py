from DB.Mark_DB import Mark_DB_Fun
import tkinter
from tkinter import *

def Mark_Manuallly_Fun():
    def Mark_Manually():
        Mark_DB_Fun(entry_1.get())
    root8=Tk()
    root8.geometry('400x350')
    # root8.attributes('-topmost', True)
    root8.configure(bg="#6B7AA1")
    root8.title("Mark Manual Attendance")
    root8.resizable(0,0)
    
    label_0 = Label(root8, text="Mark Attendance",font=("bold", 30),bg="#6B7AA1")
    label_0.place(x=40,y=15)

    label_1 = Label(root8, text="Student Id :",width=20,font=("bold", 10),bg="#6B7AA1")
    label_1.place(x=70,y=140)

    entry_1 = Entry(root8)
    entry_1.place(x=200,y=140)

    but_add=Button(root8, text='Add Student',activebackground="#2C394B",bg="#2C394B",fg="#ffffff",command=Mark_Manually).place(x=150,y=200)
    root8.mainloop()
Mark_Manuallly_Fun()