# buttons - when clicked, it does stuff

from tkinter import *

count = 0

def click():
    global count
    count += 1
    print(count)

window = Tk()

photo = PhotoImage(file='python/images/vs.png')

button = Button(window,text="Click Me!",command=click,font=("Time New Roman",30),
                fg="lightblue",bg="black",
                activeforeground="lightgreen",activebackground="black",
                state=ACTIVE,
                image=photo,compound='bottom')
button.pack()

window.mainloop()