# frames -  a rectangular container to group and hold widgets 
from tkinter import *

window = Tk()
window.geometry('400x200')
window.config(background='grey')

frame = Frame(window,bg="lightblue",bd=5,relief=RAISED)
frame.place(x=35,y=20)

Button(frame,text="V",font=("Times New Roman",25),width=3).pack(side=TOP)
Button(frame,text="I",font=("Times New Roman",25),width=3).pack(side=LEFT)
Button(frame,text="T",font=("Times New Roman",25),width=3).pack(side=LEFT)
Button(frame,text="P",font=("Times New Roman",25),width=3).pack(side=LEFT)
Button(frame,text="A",font=("Times New Roman",25),width=3).pack(side=LEFT)
Button(frame,text="Y",font=("Times New Roman",25),width=3).pack(side=LEFT)


window.mainloop()