# keyboard events
from tkinter import *

def doSomething(event):
    print("You pressed: "+event.keysym)
    label.config(text=event.keysym)

window = Tk()
window.geometry("200x50")

window.bind("<Key>",doSomething)

label = Label(window,font=("Times New Roman",20))
label.pack()

window.mainloop()