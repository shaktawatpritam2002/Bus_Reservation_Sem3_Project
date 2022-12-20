from tkinter import *
from tkinter import messagebox
import sqlite3
root = Tk()

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

def add():

    con=sqlite3.connect('bus_reservation_211b225.db')
    c=con.cursor()
    
    St_name=station_ent.get() 
    St_id=id_ent.get() 
    Rt_id=route_ent.get() 

    if( St_id=='' or St_name=='' or Rt_id==''):
        messagebox.showwarning("Warning", "Please fill all the details")
    else:
        c.execute('''insert into route_details(route_id,station_name,station_id) values (?,?,?)''',(Rt_id,St_name,St_id))

        con.commit()
        con.close()
    
        messagebox.showinfo("Route entry update", "Route updated succesully")

def delete():
    con=sqlite3.connect('bus_reservation_211b225.db')
    c=con.cursor()
    
    St_name=station_ent.get() 
    St_id=id_ent.get() 
    Rt_id=route_ent.get() 

    if( St_id=='' or St_name=='' or Rt_id==''):
        messagebox.showwarning("Warning", "Please fill all the details")
    else:

        c.execute('''delete from route_details where route_id=? and station_name=? and station_id=?''',(Rt_id,St_name,St_id))
    
        con.commit()
        con.close()
    
        messagebox.showinfo("Route entry update", "Route deleted succesully")
              
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

title = Label(root, text = "Add Bus Route Details" , fg = 'green' , font = 'Arian 14 bold')
title.grid(row = 6, column = 0, columnspan = 10)

blank = Label(root, text = "                            " )
blank.grid(row = 7, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 8, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 9, column = 0)

route_text = Label(root, text = "Route Id")
route_text.grid(row=10, column=0)

Label(root, text = "Format Ex. UKR0").grid(row=9,column=1)
route_ent = Entry(root)
route_ent.grid(row=10, column=1)


station_text = Label(root, text = "Station Name")
station_text.grid(row=10, column=2)

Label(root, text = "Format Ex. Guna").grid(row=9,column=3)
station_ent = Entry(root)
station_ent.grid(row=10, column=3)

Label(root, text = "Format Ex. 0").grid(row=9,column=5)
id_text = Label(root, text = "Station Id")
id_text.grid(row=10, column=4)

id_ent = Entry(root)
id_ent.grid(row=10, column=5)

add_but = Button(root, text = "Add Route", bg ="lightgreen" ,command= add)
add_but.grid(row = 10, column = 7)

edit_but = Button(root, text = "Delete Route", fg = "red", bg = "lightgreen",command=delete)
edit_but.grid(row = 10, column = 8)

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

house_but = Button(root, image=house, command=home)
house_but.grid(row = 14, column = 6)

def back():
    root.destroy()
    import new_detail_to_database

back_but = Button(root, text='Go Back', command=back)
back_but.grid(row = 14, column = 9)

root.mainloop()