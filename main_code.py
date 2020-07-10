from tkinter import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('studentdate.db')
cObj = con.cursor()

gui= Tk ()
gui.title("Student Data")
gui.iconbitmap('student.ico')

def refresh_data():
    for data in gui.winfo_children():
        data.destroy()
        My_head()
        my_code()
#        app_navigation()

#for menu bar

#def app_navigation():
#    def clear_all():
#        cObj.execute("DELETE FROM coin")
#        con.commit()

#        messagebox.showinfo("Notification", "Student Data Cleared")
#        refresh_data()

#    def close_app():
#        gui.destroy()

#    menu = Menu(gui)
#    file_item = Menu(menu)
#    file_item.add_command(label='Clear Data', command=clear_all)
#    file_item.add_command(label='Close App', command=close_app)
#    menu.add_cascade(label="File", menu=file_item)
#    gui.config(menu=menu)

def my_code():

    def add_student():
        cObj.execute("INSERT INTO studentdata(fname,lname,dept_name) values(?,?,?)",(fname_add.get(),lname_add.get(),dept_add.get()))
        con.commit()
        messagebox.showinfo("Notification", "New Student Data Inserted")
        refresh_data()

    def update_student():
        cObj.execute("UPDATE studentdata SET fname=?,lname=?,dept_name=? WHERE roll_no=?",(fname_up.get(),lname_up.get(),dept_up.get(),rollno_up.get()))
        con.commit()
        messagebox.showinfo("Notification", "Student Data Updated")
        refresh_data()

    def remove_student():
        cObj.execute("DELETE FROM studentdata WHERE roll_no=?",(roll_no_re.get(),))
        con.commit()
        messagebox.showwarning("Notification", "Student Data Cleared")
        refresh_data()

    idx_row=2
    cObj.execute("Select * from studentdata")
    task=cObj.fetchall()
    for item in task:
        roll_no = Label(gui,text=item[0],bg='snow',fg='black' ,font="lato 12 ",padx='5',pady='5',borderwidth=3,relief='groove')
        roll_no.grid(row=idx_row,column=0,sticky=N+S+E+W)

        F_name = Label(gui,text=item[1],bg='snow',fg='black',font="lato 12 ",padx='5',pady='5',borderwidth=3,relief='groove')
        F_name.grid(row=idx_row,column=1,sticky=N+S+E+W)

        L_name = Label(gui,text=item[2],bg='snow',fg='black',font="lato 12 ",padx='5',pady='5',borderwidth=3,relief='groove')
        L_name.grid(row=idx_row,column=2,sticky=N+S+E+W)

        Dept = Label(gui,text=item[3],bg='snow',fg='black',font="lato 12 ",padx='5',pady='5',borderwidth=3,relief='groove')
        Dept.grid(row=idx_row,column=3,sticky=N+S+E+W)

        idx_row +=1
    #to make blank column

    div = Label(gui,text="",bg='black',padx='5',pady='5',borderwidth=3,relief='groove')
    div.grid(row=0,column=5,rowspan=idx_row,sticky=N+S+E+W)

    #Entry Block for add student
    fname_add=Entry(gui,borderwidth=3,relief='groove')
    fname_add.grid(row=2,column=7,sticky=N+S+E+W)

    lname_add=Entry(gui,borderwidth=3,relief='groove')
    lname_add.grid(row=2,column=8,sticky=N+S+E+W)

    dept_add=Entry(gui,borderwidth=3,relief='groove')
    dept_add.grid(row=2,column=9,sticky=N+S+E+W)

    add = Button(gui,text='Add Student',bg='Black',fg='snow',font='lato 12 bold',command=add_student,padx='5',pady='5',borderwidth=3,relief='groove')
    add.grid(row=2,column=10,sticky=N+S+E+W)

    #Entry block for Update student
    rollno_up=Entry(gui,borderwidth=3,relief='groove')
    rollno_up.grid(row=3,column=6,sticky=N+S+E+W)

    fname_up=Entry(gui,borderwidth=3,relief='groove')
    fname_up.grid(row=3,column=7,sticky=N+S+E+W)

    lname_up=Entry(gui,borderwidth=3,relief='groove')
    lname_up.grid(row=3,column=8,sticky=N+S+E+W)

    dept_up=Entry(gui,borderwidth=3,relief='groove')
    dept_up.grid(row=3,column=9,sticky=N+S+E+W)

    update = Button(gui,text='Update',bg='Black',fg='snow',font='lato 12 bold',command=update_student,padx='5',pady='5',borderwidth=3,relief='groove')
    update.grid(row=3,column=10,sticky=N+S+E+W)

    #Entry block for Delete Student

    roll_no_re=Entry(gui,borderwidth=3,relief='groove')
    roll_no_re.grid(row=4,column=6,sticky=N+S+E+W)

    remove = Button(gui,text='Remove',bg='Black',fg='snow',font='lato 12 bold',command=remove_student,padx='5',pady='5',borderwidth=3,relief='groove')
    remove.grid(row=4,column=10,sticky=N+S+E+W)

    refresh = Button(gui,text="R E F R E S H",bg='red',fg='Snow' ,font="lato 12 bold",padx='5',command=refresh_data,pady='5',borderwidth=3,relief='groove')
    refresh.grid(row=4,column=7,columnspan=3,sticky=N+S+E+W)

def My_head():
    #Heading Bar
    portid = Label(gui,text="Show Student Data",bg='Black',fg='Snow' ,font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
    portid.grid(row=0,column=0,columnspan=4,sticky=N+S+E+W)

    #Sub heading to see student details

    rollno = Label(gui,text="Roll_No",bg='grey',fg='Snow' ,font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
    rollno.grid(row=1,column=0,sticky=N+S+E+W)

    Fname = Label(gui,text="First_Name",bg='grey',fg='Snow' ,font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
    Fname.grid(row=1,column=1,sticky=N+S+E+W)

    Lname = Label(gui,text="Last_Name",bg='grey',fg='Snow' ,font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
    Lname.grid(row=1,column=2,sticky=N+S+E+W)

    Dept = Label(gui,text="Dept_Name",bg='grey',fg='Snow' ,font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
    Dept.grid(row=1,column=3,sticky=N+S+E+W)


    #sub heading for changing partk
    sub = Label(gui,text="Change Student Data",bg='Black',fg='Snow' ,font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
    sub.grid(row=0,column=6,columnspan=5,sticky=N+S+E+W)

    rollno = Label(gui,text="Roll_No",bg='grey',fg='Snow' ,font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
    rollno.grid(row=1,column=6,sticky=N+S+E+W)

    Fname = Label(gui,text="First_Name",bg='grey',fg='Snow' ,font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
    Fname.grid(row=1,column=7,sticky=N+S+E+W)

    Lname = Label(gui,text="Last_Name",bg='grey',fg='Snow' ,font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
    Lname.grid(row=1,column=8,sticky=N+S+E+W)

    Dept = Label(gui,text="Dept_Name",bg='grey',fg='Snow' ,font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
    Dept.grid(row=1,column=9,sticky=N+S+E+W)


    ctype = Label(gui,text="Make change",bg='grey',fg='Snow' ,font="lato 12 bold",padx='5',pady='5',borderwidth=3,relief='groove')
    ctype.grid(row=1,column=10,sticky=N+S+E+W)

My_head()
my_code()
#app_navigation()

gui.mainloop()
cObj.close()
con.close()