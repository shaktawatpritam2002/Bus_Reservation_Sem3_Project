from tkinter import *
from tkinter import messagebox
import sqlite3
root = Tk()

def add():
    con=sqlite3.connect('bus_reservation_211b225.db')
    c=con.cursor()
    
    Op_id=id_ent.get() 
    Op_name=name_ent.get()
    Op_add=address_ent.get()
    Phone=phone_ent.get()
    Email=email_ent.get()

    c.execute('''select operator_id from operator where operator_id=?''',(Op_id,))
    an=c.fetchone()
    
    if( Op_id=='' or Op_name=='' or Op_add=='' or Phone=='' or Email==''):
        messagebox.showwarning("Warning", "Please fill all the details")
    elif(an!=[]):
        messagebox.showwarning("Warning", "Operator id already exist")
    
    elif(len(Phone)!=11):
        messagebox.showwarning("Warning", "Please enter valid phone number")
    else:

        c.execute('''insert into operator(operator_name,operator_id,address,phone,email) values (?,?,?,?,?)''',(Op_name,Op_id,Op_add,Phone,Email))
    
        Label(root,text=" Operator details" ,font="Arial 12 bold",fg='green').grid(row=18,column=3,columnspan=5)
        Label(root,text=" Operator name" ,font="Arial 12 bold").grid(row=19,column=3)
        Label(root,text=" Operator ID" ,font="Arial 12 bold").grid(row=19,column=4)
        Label(root,text=" Operator Address" ,font="Arial 12 bold").grid(row=19,column=5)
        Label(root,text=" Phone" ,font="Arial 12 bold").grid(row=19,column=6)
        Label(root,text=" Email" ,font="Arial 12 bold").grid(row=19,column=7)

        Label(root,text=" "+Op_name+" ").grid(row=20,column=3)
        Label(root,text=" "+Op_id+" ").grid(row=20,column=4)
        Label(root,text=" "+Op_add+" ").grid(row=20,column=5)
        Label(root,text=" "+Phone+" ").grid(row=20,column=6)
        Label(root,text=" "+Email+" ").grid(row=20,column=7)
        con.commit()
        con.close()
    
        messagebox.showinfo("operator entry update", "operator record updated succesully")

def edit():
    con=sqlite3.connect('bus_reservation_211b225.db')
    c=con.cursor()
    
    Op_id=id_ent.get() 
    Op_name=name_ent.get()
    Op_add=address_ent.get()
    Phone=phone_ent.get()
    Email=email_ent.get()   
    

    c.execute('''select operator_id from operator where operator_id=?''',(Op_id,))
    an=c.fetchone()
    
    if( Op_id=='' or Op_name=='' or Op_add=='' or Phone=='' or Email==''):
        messagebox.showwarning("Warning", "Please fill all the details")
    
    elif(len(Phone)!=11):
        messagebox.showwarning("Warning", "Please enter valid phone number")
    else:

        c.execute('''update operator set operator_name=?,operator_id=?,address=?,phone=?,email=? where operator_id=?''',(Op_name,Op_id,Op_add,Phone,Email,Op_id))
        
        Label(root,text=" Operator details" ,font="Arial 12 bold",fg='green').grid(row=17,column=3,columnspan=5)
        Label(root,text=" Operator name" ,font="Arial 12 bold").grid(row=18,column=3)
        Label(root,text=" Operator ID" ,font="Arial 12 bold").grid(row=18,column=4)
        Label(root,text=" Operator Address" ,font="Arial 12 bold").grid(row=18,column=5)
        Label(root,text=" Phone" ,font="Arial 12 bold").grid(row=18,column=6)
        Label(root,text=" Email" ,font="Arial 12 bold").grid(row=18,column=7)

        Label(root,text=" "+Op_name+" ").grid(row=19,column=3)
        Label(root,text=" "+Op_id+" ").grid(row=19,column=4)
        Label(root,text=" "+Op_add+" ").grid(row=19,column=5)
        Label(root,text=" "+Phone+" ").grid(row=19,column=6)
        Label(root,text=" "+Email+" ").grid(row=19,column=7)

        con.commit()
        con.close()
    
        messagebox.showinfo("operator entry update", "operator record updated succesully")


h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
            
bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 0, columnspan = 12, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 0)

title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'Arian 20 bold')
title.grid(row = 2, column = 0, columnspan = 12)

blank = Label(root, text = "                            " )
blank.grid(row = 3, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 4, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)

add_text = Label(root, text = "Add Bus Operator Details",  fg = "green", font = 'Arian 20 bold')
add_text.grid(row = 6, column = 0, columnspan = 12)

blank = Label(root, text = "                            " )
blank.grid(row = 7, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 8, column = 0)



id_text = Label(root, text = "Operator id")
id_text.grid(row = 10, column = 0)

Label(root, text = "Format Ex. OPUK0").grid(row=9,column=1)
id_ent = Entry(root, width= 10)
id_ent.grid(row = 10, column =1)


name_text = Label(root, text = "Name")
name_text.grid(row = 10, column = 2)


name_ent = Entry(root)
name_ent.grid(row = 10, column =3)


address_text = Label(root, text = "Address")
address_text.grid(row = 10, column = 4)

address_ent = Entry(root)
address_ent.grid(row = 10, column =5)


phone_text = Label(root, text = "Phone")
phone_text.grid(row = 10, column = 6)

Label(root, text = "Format Ex. 03440123456").grid(row=9,column=7)
phone_ent = Entry(root)
phone_ent.grid(row = 10, column =7)


email_text = Label(root, text = "Email")
email_text.grid(row = 10, column = 8)

email_ent = Entry(root)
email_ent.grid(row = 10, column =9)

add_but = Button(root, text = "Add", bg= "lightgreen" , command=add)
add_but.grid(row =10, column = 10)

edit_but = Button(root, text = "Edit", bg = "lightgreen", command = edit)
edit_but.grid(row =10, column = 11)

blank = Label(root, text = "                            " )
blank.grid(row = 11, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 12, column = 0)

def home():
    root.destroy()
    import home

houses = PhotoImage(file = ".\\home.png")
Button(root, image = houses , command=home).grid(row = 14, column = 6)

def back():
    root.destroy()
    import new_detail_to_database

back_but = Button(root, text='Go Back', command=back)
back_but.grid(row = 14, column = 9)

root.mainloop()