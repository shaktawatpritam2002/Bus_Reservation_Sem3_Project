from tkinter import *
import sqlite3
from tkinter import messagebox
root = Tk()


def add_run():
    con=sqlite3.connect('bus_reservation_211b225.db')
    c=con.cursor()
    ID=route_ent.get()
    Date=station_ent.get()
    Seat=id_ent.get()

    if( ID=='' or Date=='' or Seat==''):
        messagebox.showwarning("Warning", "Please fill all the details")
    else:

        c.execute('''insert into running_details(running_bus_id,running_date,a_seat) values (?,?,?)''',(ID,Date,Seat))
        con.commit()
        con.close()
        messagebox.showinfo("message", "Record Added Successfully")



def delete_run():
    con=sqlite3.connect('bus_reservation_211b225.db')
    c=con.cursor()
    ID=route_ent.get()
    Date=station_ent.get()

    if( ID=='' or Date=='' ):
        messagebox.showwarning("Warning", "Please fill all the details")
    else:

        c.execute(''' delete from running_details where running_bus_id=? and running_date=?''',(ID,Date))
        con.commit()
        con.close()
        messagebox.showinfo("Delete", "Record Deleted Successfully")



h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 0, columnspan = 10, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 1)

title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'Arian 14 bold')
title.grid(row = 2, column = 0, columnspan = 10)

blank = Label(root, text = "                            " )
blank.grid(row = 3, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 4, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)

title = Label(root, text = "Add Bus Running Details" , fg = 'green' , font = 'Arian 14 bold')
title.grid(row = 6, column = 0, columnspan = 10)

blank = Label(root, text = "                            " )
blank.grid(row = 7, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 8, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 9, column = 0)

route_text = Label(root, text = "Bus Id")
route_text.grid(row=10, column=0)

Label(root, text = "Format Ex. UK0B0").grid(row=9,column=1)
route_ent = Entry(root)
route_ent.grid(row=10, column=1)

station_text = Label(root, text = "Running Date")
station_text.grid(row=10, column=2)
Label(root, text = "Format Ex. 2022-12-28").grid(row=9,column=3)
station_ent = Entry(root)
station_ent.grid(row=10, column=3)

id_text = Label(root, text = "Seat Available")
id_text.grid(row=10, column=4)

id_ent = Entry(root)
id_ent.grid(row=10, column=5)

add_but = Button(root, text = "Add Run", bg ="lightgreen",command=add_run)
add_but.grid(row = 10, column = 6)

edit_but = Button(root, text = "Delete Run", bg = "lightgreen", command=delete_run)
edit_but.grid(row = 10, column = 7)

blank = Label(root, text = "                            " )
blank.grid(row = 11, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 12, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 13, column = 0)

house = PhotoImage(file = ".\\home.png")

def home():
    root.destroy()
    import home
house_but = Button(root, image=house,command=home)
house_but.grid(row = 14, column = 6)

def back():
    root.destroy()
    import new_detail_to_database

back_but = Button(root, text='Go Back', command=back)
back_but.grid(row = 14, column = 7)

root.mainloop()
