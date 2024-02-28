from tkinter import *
from tkinter.ttk import *
def submit():
    F1 = e1.get()
    F2 = e2.get()
    R = e3.get()
    if F1 == "" or F2 == "" or R == "":
        ErrorWindow()
        return
    else:
        Submitted = Toplevel(master)
        Submitted.title("Submitted")
        Label(Submitted, text='Application has been successfully submitted').grid(row=0)
        button = Button(Submitted, text='Exit', width=10, command=master.destroy).grid(row=1)
        f = open("Applications.txt", "a")
        f.write("Name: " + F1 + " " + F2 + "\nWhy they want to work for us: " + R)
master = Tk()
def ErrorWindow():
    Error = Toplevel(master)
    Error.title("Error")
    Label(Error, text='Error, not all fields have been filled out').grid(row=0)
    button = Button(Error, text='Return', width=10, command=Error.destroy).grid(row=2)
Label(master, text='Please enter first and last name').grid(row=0)
Label(master, text='First Name').grid(row=1)
Label(master, text='Last Name').grid(row=2)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
Label(master, text='Why are you interested in working for us?').grid(row=3)
e3 = Entry(master)
e3.grid(row=4)
button = Button(master, text='Stop', width=10, command=master.destroy).grid(row=5, column=0)
button1 = Button(master, text='Submit', width=10, command=submit).grid(row=5, column=1)
mainloop()