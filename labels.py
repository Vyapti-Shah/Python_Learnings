#labels - an area widget that holds text and/or an image within a window 
from tkinter import *

window = Tk()

window.geometry("500x500") # x = ex 

photo = PhotoImage(file='python/images/vs.png')

label = Label(window,text="Hello World",
              font=('Times New Roman',20,'bold'),
              fg='lightblue',
              bg='black',
              relief=RAISED,
              bd=10,padx=20,pady=10,
              image=photo,
              compound='bottom') #fg=foreground #bd=border width
label.pack()

label1 = Label(window,text="I am Vyapti Shah",font=('Times New Roman',15))
label1.place(x=0,y=250)

window.mainloop()