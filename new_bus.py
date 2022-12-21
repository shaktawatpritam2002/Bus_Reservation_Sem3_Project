import string
from tkinter import *
from tkinter import messagebox
import sqlite3
root = Tk()
h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

clicked = StringVar()
clicked.set("AC 2+2")
              
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

title = Label(root, text = "Add Bus Details" , fg = 'green' , font = 'Arian 14 bold')
title.grid(row = 6, column = 0, columnspan = 10)

blank = Label(root, text = "                            " )
blank.grid(row = 7, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 8, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 9, column = 0)

add_bus = Label(root, text = "Bus ID")
add_bus.grid(row=10, column=0)

Label(root, text = "Format Ex. UK0B0").grid(row=9,column=1)
ent_bus = Entry(root)
ent_bus.grid(row=10, column=1)

type_bus = Label(root, text = "Bus Type")
type_bus.grid(row=10, column=2)

drop_bus = OptionMenu(root, clicked ,"AC 2+2", "AC 3+2", "Non AC2+2", "Non AC 3+2", "AC-Sleeper 2+1", "Non-AC SLeeper 2+1" )
drop_bus.grid(row=10, column=3)
BUS_TYPE=clicked.get()

capacity_text = Label(root, text = "Capacity")
capacity_text.grid(row=10, column=4)

cap_ent = Entry(root)
cap_ent.grid(row=10, column=5)

fare_text = Label(root, text = "Fare Rs")
fare_text.grid(row=10, column=6)

fare_ent = Entry(root)
fare_ent.grid(row=10, column=7)


opt_text = Label(root, text = "Operator ID")
opt_text.grid(row=10, column=8)

Label(root, text = "Format Ex. OPUK1").grid(row=9,column=9)
opt_ent = Entry(root)
opt_ent.grid(row=10, column=9)

route_text = Label(root, text = "Route ID")
route_text.grid(row=10, column=10)

Label(root, text = "Format Ex. UKR0").grid(row=9,column=11)
route_ent = Entry(root)
route_ent.grid(row=10, column=11)

blank = Label(root, text = "                            " )
blank.grid(row = 12, column = 0)

blank = Label(root, text = "                            " )
blank.grid(row = 14, column = 0)

def add_record():
    Add_Bus=ent_bus.get()
    BUS_TYPE=clicked.get()
    Capacity=cap_ent.get()
    Fare=fare_ent.get()
    Op_id=opt_ent.get()
    Rt_id=route_ent.get()
    
    con=sqlite3.connect('bus_reservation_211b225.db')
    c=con.cursor()
    c.execute(''' select op_name from bus_details where op_id=?''',(Op_id,))
    r=c.fetchall()
    for i in r:
        Label(root,text=" "+Add_Bus+" "+r[0]+" ").grid(row=14,column=2,columnspan=3)
    
    
    c.execute('''insert into bus_details (bus_id,bus_type,seat_capacity,fare,op_id,rt_id) values (?,?,?,?,?,?)''',(Add_Bus,BUS_TYPE,Capacity,Fare,Op_id,Rt_id))
    
    # c.execute(''' UPDATE bus_details SET op_name=? WHERE OP_ID=? AND BUS_ID=?''',(Op_name,Op_id,Add_Bus))
    Label(root,text=" Bus Details" ,font="Arial 12 bold",fg='green').grid(row=17,column=3,columnspan=5)
    Label(root,text=" Bus ID" ,font="Arial 12 bold").grid(row=18,column=3)
    Label(root,text=" Bus Type" ,font="Arial 12 bold").grid(row=18,column=4)
    Label(root,text=" Seat Capacity" ,font="Arial 12 bold").grid(row=18,column=5)
    Label(root,text=" Fare" ,font="Arial 12 bold").grid(row=18,column=6)
    Label(root,text=" Operator ID" ,font="Arial 12 bold").grid(row=18,column=7)
    Label(root,text=" Route ID" ,font="Arial 12 bold").grid(row=18,column=8)

    Label(root,text=" "+Add_Bus+" ").grid(row=19,column=3)
    Label(root,text=" "+BUS_TYPE+" ").grid(row=19,column=4)
    Label(root,text=" "+Capacity+" ").grid(row=19,column=5)
    Label(root,text=" "+Fare+" ").grid(row=19,column=6)
    Label(root,text=" "+Op_id+" ").grid(row=19,column=7)
    Label(root,text=" "+Rt_id+" ").grid(row=19,column=8)
    con.commit()
    con.close()
    messagebox.showinfo("bus entry", "Bus record added")

def edit_record():
    Add_Bus=ent_bus.get()
    BUS_TYPE=clicked.get()
    Capacity=cap_ent.get()
    Fare=fare_ent.get()
    Op_id=opt_ent.get()
    Rt_id=route_ent.get()
    
    con=sqlite3.connect('bus_reservation_211b225.db')
    c=con.cursor()
    

    c.execute('''update bus_details SET bus_type=?,seat_capacity=? ,op_id=?, rt_id=?, fare=? where bus_id=?''',(BUS_TYPE,Capacity,Op_id,Rt_id,Fare,Add_Bus))
    
    # c.execute(''' UPDATE bus_details SET op_name=? WHERE OP_ID=? AND BUS_ID=?''',(Op_name,Op_id,Add_Bus))
     # c.execute(''' UPDATE bus_details SET op_name=? WHERE OP_ID=? AND BUS_ID=?''',(Op_name,Op_id,Add_Bus))
    Label(root,text=" Bus Details" ,font="Arial 12 bold",fg='green').grid(row=17,column=3,columnspan=5)
    Label(root,text=" Bus ID" ,font="Arial 12 bold").grid(row=18,column=3)
    Label(root,text=" Bus Type" ,font="Arial 12 bold").grid(row=18,column=4)
    Label(root,text=" Seat Capacity" ,font="Arial 12 bold").grid(row=18,column=5)
    Label(root,text=" Fare" ,font="Arial 12 bold").grid(row=18,column=6)
    Label(root,text=" Operator ID" ,font="Arial 12 bold").grid(row=18,column=7)
    Label(root,text=" Route ID" ,font="Arial 12 bold").grid(row=18,column=8)

    Label(root,text=" "+Add_Bus+" ").grid(row=19,column=3)
    Label(root,text=" "+BUS_TYPE+" ").grid(row=19,column=4)
    Label(root,text=" "+Capacity+" ").grid(row=19,column=5)
    Label(root,text=" "+Fare+" ").grid(row=19,column=6)
    Label(root,text=" "+Op_id+" ").grid(row=19,column=7)
    Label(root,text=" "+Rt_id+" ").grid(row=19,column=8)
    con.commit()
    con.close()
    messagebox.showinfo("bus entry", "Bus record edited")

add_but = Button(root, text = "Add Bus", bg='bisque3', command=add_record)
add_but.grid(row = 15, column = 6)

edit_but = Button(root, text = "Edit Bus",bg='salmon2', command=edit_record)
edit_but.grid(row = 15, column = 7)

house = PhotoImage(file = ".\\home.png")

def home():
    root.destroy()
    import home

house_but = Button(root, image=house, command=home)
house_but.grid(row = 15, column = 8)

def back():
    root.destroy()
    import new_detail_to_database

back_but = Button(root, text='Go Back',bg='skyblue3', command=back)
back_but.grid(row = 15, column = 9)

root.mainloop()
