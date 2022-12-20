from tkinter import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

bus_img=PhotoImage(file='.\\Project\Bus_for_project.png')
Label(root,image=bus_img).pack()
#grid(row=0,column=0,padx=550)

Label(root,text="Online Bus Booking System", bg='LightSkyBlue1', font="Arial 18 bold" , fg='red2' ).pack()

Label(root,text="\n\n\n\nName : Pritm Singh Shaktawat\n\n\nEr : 211B225\n\n\nMobile : 9079009294\n\n\n\n", font="Arial 12 bold" , fg='medium blue' ).pack()

Label(root,text="Submitted  to : Dr. Mahesh Kumar", bg='LightSkyBlue1', font="Arial 18 bold" , fg='red2' ).pack()

Label(root,text="Project Based Learning", font="Arial 14" , fg='red2' ).pack()

def next(a=0):
    root.destroy()
    import home

root.bind('<KeyPress>',next)
