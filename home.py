from tkinter import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

bus_img=PhotoImage(file='.\\Project\Bus_for_project.png')
Label(root,image=bus_img).grid(row=0,column=2,columnspan=3,padx=w/3+80)
#grid(row=0,column=0,padx=550)

Label(root,text="Online Bus Booking System", bg='LightSkyBlue1', font="Arial 18 bold" , fg='red2' ).grid(row=1,column=2,columnspan=3)

Label(root,text="\n\n").grid(row=2,column=2)

def seat():
    root.destroy()
    import journey_details

Button(root,text="Seat Booking", bg='chartreuse3', font="Arial 16 bold", command=seat).grid(row=3,column=2)

def booked():
    root.destroy()
    import check_booking

Button(root,text="check Booked Seat", bg='green2', font="Arial 16 bold" , command=booked).grid(row=3,column=3 )

def addbus():
    root.destroy()
    import new_detail_to_database

Button(root,text="Add Bus Details", bg='green4', font="Arial 16 bold" , command=addbus).grid(row=3,column=4)

Label(root,text="For Admin Only",font="Arial 12", fg='red1').grid(row=4,column=4,pady=25)
