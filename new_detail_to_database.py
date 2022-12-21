from tkinter import *
root = Tk()

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

              
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

detail = Label(root, text = "Add New Details to Database", fg ="green", font = 'Arian 14 bold')
detail.grid(row = 6, column = 0, columnspan = 3)

blank = Label(root, text = "                            " )
blank.grid(row = 7, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 8, column = 0)

def n_op():
    root.destroy()
    import new_operator

operator_but= Button(root, text ="New Operator", bg = "lightgreen", command=n_op)
operator_but.grid(row= 9, column=0)


def n_bus():
    root.destroy()
    import new_bus

bus_but= Button(root, text ="New Bus", bg = "deep pink", command=n_bus)
bus_but.grid(row= 9, column=1)

def n_route():
    root.destroy()
    import new_route

route_but= Button(root, text ="New Route", bg = "lightblue", command=n_route)
route_but.grid(row= 9, column=2)

def n_run():
    root.destroy()
    import new_run

run_but= Button(root, text ="New Run", bg = "red3", command=n_run)
run_but.grid(row= 9, column=3)


blank = Label(root, text = "                            " )
blank.grid(row = 10, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 11, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 12, column = 0)

def home():
    root.destroy()
    import home

house = PhotoImage(file = ".\\home.png")
house_but = Button(root, image=house, command=home)
house_but.grid(row = 13, column = 1)


def back():
    root.destroy()
    import home

back_but = Button(root, text='Go Back', command=back)
back_but.grid(row = 14, column = 1)
root.mainloop()
