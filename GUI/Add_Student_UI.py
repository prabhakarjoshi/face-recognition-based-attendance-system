# import tkinter
from tkinter import *
from tkinter import font 
from DB.Add_New_Student import Add_New_Student_Fun

def  Add_Student_UI_Fun():
    root5=Tk()
    var1=StringVar()

    def Add_New_Student_Fun_Helper():
        Add_New_Student_Fun(root5,entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get(),var1.get())
        print("K")


    
    root5.geometry('500x450')
    root5.attributes('-topmost', True)
    root5.configure(bg="#6B7AA1")
    root5.title("New Registration")
    root5.resizable(0,0)
    
    label_0 = Label(root5, text="Register a student",font=("bold", 40),bg="#6B7AA1")
    label_0.place(x=20,y=15)

    label_1 = Label(root5, text="Student Name :",width=20,font=("bold", 10),bg="#6B7AA1")
    label_1.place(x=80,y=140)

    entry_1 = Entry(root5)
    entry_1.place(x=280,y=140)


    label_2 = Label(root5, text="Section :",width=20,font=("bold", 10),bg="#6B7AA1")
    label_2.place(x=80,y=180)

    entry_2 = Entry(root5)
    entry_2.place(x=280,y=182)

    label_3 = Label(root5, text="Student ID :",width=20,font=("bold", 10),bg="#6B7AA1")
    label_3.place(x=80,y=220)

    entry_3 = Entry(root5)
    entry_3.place(x=280,y=220)

    label_4 = Label(root5, text="Roll No",width=20,font=("bold", 10),bg="#6B7AA1")
    label_4.place(x=80,y=260)

    entry_4 = Entry(root5)
    entry_4.place(x=280,y=262)

    label_5 = Label(root5, text="Course :",width=20,font=("bold", 10),bg="#6B7AA1")
    label_5.place(x=80,y=300)

    
    list1=["B-Tech","MBA",'BCA','BSc',"MSc",'M-Tech']
    droplist=OptionMenu(root5,var1,*list1)
    var1.set("Select Course")
    # droplist.config(width=15)
    
    droplist.place(x=280,y=300)

    but_add=Button(root5, text='ADD',width=12,bg='brown',fg='white',command=Add_New_Student_Fun_Helper)
    but_add.place(x=200,y=360)


    root5.mainloop()
# Add_Student_UI_Fun()