from tkinter import *
from tkinter import messagebox 
root = Tk()

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
    

bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 1, columnspan = 3, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 1)

title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'Arial 14 bold')
title.grid(row = 2, column = 1, columnspan = 3, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 3, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 4, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)

ticket_text = Label(root, text ="Bus Ticket", font=' Arial 14 bold',fg='Red')
ticket_text.grid(row = 6, column=1, columnspan=3)

final = LabelFrame(root)
final.grid(row = 7, column =1, columnspan=3)

passenger_text = Label(final, text = "Passenger: ")
passenger_text.grid(row =8, column=0)

age_text = Label(final, text = "Age: ")
age_text.grid(row =12, column=0)

travel_text = Label(final, text = "Travel On: ")
travel_text.grid(row =14, column=0)

seats_text = Label(final, text = "Number of Seats ")
seats_text.grid(row =16, column=0)

g_text = Label(final, text = "Gender: ")
g_text.grid(row =10, column=0)

phone_text = Label(final, text = "Phone: ")
phone_text.grid(row =8, column=1)

fare_text = Label(final, text = "Fare Rs: ")
fare_text.grid(row =10, column=1)

booked_text = Label(final, text = "Booked On: ")
booked_text.grid(row =12, column=1)

detail_text = Label(final, text = "Bus Detail: ")
detail_text.grid(row =14, column=1)

booked_text = Label(final, text = "Boarding Point: ")
booked_text.grid(row =16, column=1)

last_text = Label(final, text = "Total amount in rupees you have to pay at the time of boarding the bus :")
last_text.grid(row =20, column=0)


import sqlite3
con=sqlite3.connect('bus_reservation_211b225.db')
cur=con.cursor()
        
# travel_date=ent_date.get()
# To=ent_To.get()
# From=ent_From.get()

    # mobile= Mobile1
    # booked_bus_id=rv1.get()
    # Date=ent_date.get()
cur.execute('''select max(rowid) from booking_details''')
a=cur.fetchone()
num=a[0]
cur.execute('''select name,gender,age,travelling_date,number_of_seats,mobile,fare,booking_date,op_name,station_name,total_fare from bus_details,booking_details,route_details where rowid=? and station_id=1 and bus_id=bus and route_id=rt_id''',[num])
res = cur.fetchall()
for i in res:
    Label(final,text = i[0],font='Arial 10 bold').grid(row=9,column = 0)
    Label(final,text = i[2],font='Arial 10 bold').grid(row=11,column = 0)
    Label(final,text = i[1],font='Arial 10 bold').grid(row=13,column = 0)
    Label(final,text = i[3],font='Arial 10 bold').grid(row=15,column = 0)
    Label(final,text = i[4],font='Arial 10 bold').grid(row=17,column = 0)
    Label(final,text = i[5],font='Arial 10 bold').grid(row=9,column = 1)
    Label(final,text = i[6],font='Arial 10 bold').grid(row=11,column = 1)
    Label(final,text = i[7],font='Arial 10 bold').grid(row=13,column = 1)
    Label(final,text = i[8],font='Arial 10 bold').grid(row=15,column = 1)
    Label(final,text = i[9],font='Arial 10 bold').grid(row=17,column = 1)

    Label(final,text = i[10],font='Arial 10 bold').grid(row=20,column = 1)
con.commit()
con.close()

messagebox.showinfo('Message','Seat Booked')


house = PhotoImage(file = ".\\home.png")

def home():
    root.destroy()
    import home

house_but = Button(root, image=house, command=home)
house_but.grid(row = 18, column = 2)

def back():
    root.destroy()
    import journey_details

back_but = Button(root, text='Go Back', command=back)
back_but.grid(row = 20, column = 2)

root.mainloop()
