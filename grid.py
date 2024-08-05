# grid - geometry manager that organizes widgets in a table-like structure in a parent
from tkinter import *

window = Tk()

titleLabel = Label(window,text="Enter your info",font=("Times New Roman",10)).grid(row=0,column=0,columnspan=2)

firstLabel = Label(window,text="First Name: ",width=20,bg="lightblue").grid(row=1,column=0)
firstEntry = Entry(window).grid(row=1,column=1)

lastLabel = Label(window,text="Last Name: ",bg="pink").grid(row=2,column=0)
lastEntry = Entry(window).grid(row=2,column=1)

emailLabel = Label(window,text="Email: ",bg="grey").grid(row=3,column=0)
emailEntry = Entry(window).grid(row=3,column=1)

submit_button = Button(window,text="Submit").grid(row=4,column=0,columnspan=2) #columnspan to get the submit button in the middle

window.mainloop()