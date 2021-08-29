from DB.Export_DB import Export_DB_Fun
from tkinter import *
from variables import list1,list2

def Export_UI_Fun():

    def Export_DB_Fun_Helper():
        root6.destroy()
        Export_DB_Fun(var1.get(),var2.get())   

    root6=Tk()
    root6.geometry('400x300')
    root6.title("Export")
    root6.resizable(0,0)

    var1=StringVar()
    var2=StringVar()
    var1.set("Select Course")
    var2.set("Select Section")

    label_1 = Label(root6, text="Course :",width=20, font=("bold", 10))
    label_1.place(x=40,y=40)

    droplist1=OptionMenu(root6,var1,*list1)
    droplist1.place(x=200,y=40)

    label_2 = Label(root6, text="Section :",width=20,font=("bold", 10))
    label_2.place(x=40,y=80)

    droplist2=OptionMenu(root6,var2,*list2)
    droplist2.place(x=200,y=80)


    but_Get=Button(root6, text='Export',width=12,bg='brown',fg='white',command=Export_DB_Fun_Helper)
    but_Get.place(x=150,y=180)
    root6.mainloop()
