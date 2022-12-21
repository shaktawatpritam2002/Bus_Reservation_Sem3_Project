from ctypes import cast
import string
from tkinter import *
from tkinter import messagebox
import sqlite3
import tkinter as tk
root = Tk()

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

clicked = StringVar()
clicked.set("Male")

def check_seat_age(num):
            num1=int(num)
            if(num1>0 and num1<100):
                return num.isnumeric()
            else:
                return False

def check_seat(num):
            num1=int(num)
            if(num1):
                return num.isnumeric()
            else:
                return False

def bookbus():

    def confirm ():
        Name=name_ent.get()

        Age=age_ent.get()
        p_age=int(Age)
        Seats=seats_ent.get()
        p_seat=int(Seats)
        Mobile1=''
        Mobile1=tk.StringVar()
        Mobile1=mobile_ent.get()
        Gender=clicked.get()
        T_date=ent_date.get()
        conn=sqlite3.connect('bus_reservation_211b225.db')
        c=conn.cursor()
        c.execute(''' select a_seat from running_details where running_date=? and running_bus_id=?''',(T_date,booked_bus_id))
        a=c.fetchone()
        av_seat=a[0]
        print(av_seat)
        if(Name=='' or Age=='' or Mobile1=='' or Seats==''):
            messagebox.showwarning("important","Please fill all the columns")
        elif(p_seat<1):
            messagebox.showwarning("important","Please enter correct number of seats")

        elif(av_seat<p_seat and av_seat>0):
            messagebox.showwarning("important","Seats entered are more than the available seats")
        
        elif(len(Mobile1)<10 or len(Mobile1)>10 ):
            messagebox.showwarning("important","Please enter a valid 10 digit mobile number.")

        elif( Mobile1[0]=='0'):
            messagebox.showwarning("important","Please enter valid mobile number(Mobile number can not start with 0)")
        
        elif(p_age>99 or p_age<0 ):
            messagebox.showwarning("important","It seems like you enterd wrong age. Age (0-99)")

        else:
            answer = messagebox.askyesno("Booking Confirmation", "Are you sure you want to book the bus?" )
            if answer:
                conn=sqlite3.connect('bus_reservation_211b225.db')
                c=conn.cursor()
                c.execute(''' select count(*)+1 from booking_details''')
                a=c.fetchone()
                count=a[0]
                c.execute('''insert into booking_details (name,gender,age,mobile,bus,travelling_date,booking_date,number_of_seats,rowid) values (?,?,?,?,?,?,DATE(),?,?)''',(Name,Age,Gender,Mobile1,booked_bus_id,T_date,Seats,count))

                c.execute('''update running_details set a_seat=a_seat-? where running_bus_id=? and running_date=?''',(Seats,booked_bus_id,T_date))

                c.execute('''update booking_details set total_fare=?*? where bus=?''',(Fare,Seats,booked_bus_id))
            

                conn.commit()
                conn.close()

                root.destroy()
                import ticket



    booked_bus_id=rv1.get()

    if booked_bus_id=='None':
        messagebox.showwarning("Warning", "Please select a bus")
    else:
        blank = Label(root, text = "                            " )
        blank.grid(row = 11, column = 0)

        blank = Label(root, text = "                            " )
        blank.grid(row = 12, column = 0)

        blank = Label(root, text = "                            " )
        blank.grid(row = 13, column = 0)

        blank = Label(root, text = "                            " )
        blank.grid(row = 14, column = 0)

        fill_label = Label(root, text = "Add Passenger Details" , fg = 'red' , bg = 'lightblue', font = 'Arian 14 bold')
        fill_label.grid(row = 15, column = 0, columnspan = 8)

        blank = Label(root, text = "                            " )
        blank.grid(row = 16, column = 0)

        name_text = Label(root, text = "Name")
        name_text.grid(row = 17, column=0)

        name_ent = Entry(root)
        name_ent.grid(row =17, column=1)
        Name=name_ent.get()

        gender_text = Label(root, text = "Gender")
        gender_text.grid(row = 17, column=2)

        gender_drop = OptionMenu(root, clicked , "Male", "Female", "Third Gender")
        gender_drop.grid(row = 17, column = 3)

        seats_text = Label(root, text = "No of Seats")
        seats_text.grid(row = 17, column=4)

        seats_ent = Entry(root)
        seats_ent.grid(row =17, column=5)
        Seats=seats_ent.get()

        mobile_text = Label(root, text = "Mobile No")
        mobile_text.grid(row = 17, column=6)

        mobile_ent = Entry(root)
        mobile_ent.grid(row =17, column=7)
        Mobile=mobile_ent.get()

        age_text = Label(root, text = "Age")
        age_text.grid(row = 17, column=8)

        age_ent = Entry(root)
        age_ent.grid(row =17, column=9)
        Age=age_ent.get()



        conn=sqlite3.connect('bus_reservation_211b225.db')
        c=conn.cursor()
        
        c.execute('''select fare from bus_details where bus_id=?''',(booked_bus_id,))
        m=c.fetchone()
        Fare=m[0]


        conn.commit()
        conn.close()

        book_button = Button(root, text = "Book Seat", bg ="lightgreen", command = confirm)
        book_button.grid(row = 17, column=10)

    

def showbus():

    # To=tk.StringVar()
    # From=tk.StringVar()
    # Date=tk.StringVar()

    To=ent_To.get()
    From=ent_From.get()
    Date=ent_date.get()

    conn=sqlite3.connect('bus_reservation_211b225.db')
    c=conn.cursor()
    
    c.execute('''Select op_name,bus_type,a_seat,seat_capacity,fare,bus_id from bus_details,running_details, route_details as f, route_details as t where f.station_name=? and t.station_name=? and running_date=? and running_bus_id=bus_id and f.station_id<t.station_id and f.route_id=rt_id and t.route_id=rt_id''',(From,To,Date))
    res=c.fetchall()
    
    if (To=="" or From=="" or Date==""):
        messagebox.showwarning("important","Please fill all the Column")
    elif (res==[]):
        messagebox.showwarning("important","No bus available, please change the station name or date.")
    else:
        select_text = Label(root, text = "Select Bus", fg = "black",font='Arial 12 bold')
        select_text.grid(row = 8, column=0)

        opt_text = Label(root, text = "Operator", fg = "black",font='Arial 12 bold')
        opt_text.grid(row = 8, column=1)

        type_text = Label(root, text = "Bus Type", fg = "black",font='Arial 12 bold')
        type_text.grid(row = 8, column=2)

        available_text = Label(root, text = "Available", fg = "black",font='Arial 12 bold')
        available_text.grid(row = 8, column=3)

        fare_text = Label(root, text = "Capacity", fg = "black",font='Arial 12 bold')
        fare_text.grid(row = 8, column=4)

        fare_text = Label(root, text = "Fare", fg = "black",font='Arial 12 bold')
        fare_text.grid(row = 8, column=5)


        
        num=10
    
        for i in res:
            r1=tk.Radiobutton(root,variable=rv1,value=i[5])
            r1.grid(row=num,column=0)

            operator=Label(root, text = i[0], fg = "blue1")
            operator.grid(row = num, column=1)
            b_type=Label(root, text = i[1], fg = "blue1")
            b_type.grid(row = num, column=2)
            a_seat=Label(root, text = i[2], fg = "blue1")
            a_seat.grid(row = num, column=3)
            t_seat=Label(root, text = i[3], fg = "blue1")
            t_seat.grid(row = num, column=4)
            fare=Label(root, text = i[4], fg = "blue1")
            fare.grid(row = num, column=5)
            num=num+1
    
        conn.commit()

        book_button = Button(root, text="Proceed to Book", bg = "lightgreen", command = bookbus)
        book_button.grid(row =10 , column= 6)


rv1=tk.StringVar()
rv1.set(None)
booked_bus_id=""  
Name=""
Age=""
Gender=""
Seats=""
Mobile1=""
Fare=0

bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 0, columnspan = 8, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 1)

title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'Arian 14 bold')
title.grid(row = 2, column = 0, columnspan = 8)

blank = Label(root, text = "                            " )
blank.grid(row = 3, column = 0)

title1 =Label(root, text = "Enter Journey Details", bg="lightgreen", fg = "darkgreen", font = "Arian 14 bold" )
title1.grid(row=4, column = 0, columnspan =8 )


blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)

To_text = Label(root, text = "To")
To_text.grid(row = 6, column =0)

ent_To = Entry(root, width=20)
ent_To.grid(row = 6, column =1)


From_text = Label(root, text = "From")
From_text.grid(row = 6, column =2)

ent_From = Entry(root, width=20)
ent_From.grid(row = 6, column =3)


date_text = Label(root, text = "Journey Date")
date_text.grid(row = 6, column =4)

ent_date = Entry(root, width=20)
ent_date.grid(row = 6, column =5)

date_form = Label(root, text = "Format : 'YYYY-MM-DD' ")
date_form.grid(row = 7, column =5)


show_button = Button(root, text = "Show Bus", fg = "black", bg ="green", command = showbus)
show_button.grid(row = 6, column =6)

house = PhotoImage(file = ".\\home.png")

def home():
    root.destroy()
    import home

home_button = Button(root, image = house, command=home)
home_button.grid(row =6 , column= 7)

blank = Label(root, text = "                            " )
blank.grid(row = 7, column = 0)

def back():
    root.destroy()
    import home

back_but = Button(root, text='Go Back', command=back)
back_but.grid(row = 6, column = 9)

root.mainloop()





