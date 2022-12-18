from tkinter import *
from tkinter import messagebox
root = Tk()

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

def check():

    import sqlite3
    with sqlite3.connect('bus_reservation_211b225.db') as con:
        cur=con.cursor()
    mobile= mobile_ent.get()
    if(mobile==""):
        messagebox.showwarning("Warning","Please Fill the column")
    else:
        cur.execute('''select name,gender,age,travelling_date,number_of_seats,mobile,total_fare,booking_date,op_name,station_name from bus_details,booking_details,route_details where mobile=? and station_id=1 and bus_id=bus and route_id=rt_id''',(mobile,))
        res = cur.fetchall()
        if(res==[]):
            answer=messagebox.askyesno("Message","No record found. Do you want to book now ?")
            if answer:
                root.destroy()
                import journey_details
        else:
            final = LabelFrame(root)
            final.grid(row = 8, column =0, columnspan=3)

            passenger_text = Label(final, text = "Passenger: ")
            passenger_text.grid(row =8, column=0)

            age_text = Label(final, text = "Age: ")
            age_text.grid(row =12, column=0)

            travel_text = Label(final, text = "Travel On: ")
            travel_text.grid(row =14, column=0)

            seats_text = Label(final, text = "No of Seats: ")
            seats_text.grid(row =16, column=0)

            g_text = Label(final, text = "Gender: ")
            g_text.grid(row =10, column=0)

            phone_text = Label(final, text = "Phone: ")
            phone_text.grid(row =8, column=1)

            flare_text = Label(final, text = "Fare Rs: ")
            flare_text.grid(row =10, column=1)

            booked_text = Label(final, text = "Booked On: ")
            booked_text.grid(row =12, column=1)

            point_text = Label(final, text = "Bus Detail: ")
            point_text.grid(row =14, column=1)

            booked_text = Label(final, text = "Boarding Point: ")
            booked_text.grid(row =16, column=1)

            last_text = Label(final, text = "The amount you needto pay at the time of boarding the bus")
            last_text.grid(row =20, column=0)


        

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
                
                Label(final,text = i[6],font='Arial 10 bold').grid(row=20,column = 1)
                
            con.commit()
            con.close()
              
bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 0, columnspan = 3, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 1)

title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'Arian 14 bold')
title.grid(row = 2, column = 0, columnspan = 3)

blank = Label(root, text = "                            " )
blank.grid(row = 3, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 4, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)


title1 = Label(root, text = "Check Your Booking" , fg = 'darkgreen' , bg = 'lightgreen', font = 'Arian 14 bold')
title1.grid(row = 4, column = 0, columnspan = 3)

blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 6, column = 0)

mobile_text = Label(root, text = "Enter Your Mobile No: ")
mobile_text.grid(row =7, column =0)

mobile_ent = Entry(root)
mobile_ent.grid(row =7, column=1)

check_but = Button(root, text = "Check Booking", command = check)
check_but.grid(row = 7, column=2)



root.mainloop()
