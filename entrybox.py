# entry widget - textbox that accepts a single line of user input

from tkinter import *

def submit():
    username = entry.get()
    print("Hello "+username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

window = Tk()

entry = Entry(window,font=("Times New Roman",50),bg="lightblue",fg="#323131",show="*")
entry.pack(side=LEFT)


submit_button = Button(window,text="submit",command=submit,font=("Times New Roman",20),bg="black",fg="white")
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="delete",command=delete,font=("Times New Roman",20),bg="black",fg="white")
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text="backspace",command=backspace,font=("Times New Roman",20),bg="black",fg="white")
backspace_button.pack(side=RIGHT)

window.mainloop()