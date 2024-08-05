from tkinter import *

def display():
    if(x.get()==1):
        print("You can code")
    else:
        print("You cannot code")

window = Tk()

x = IntVar() #StringVar() #BooleanVar() = onvalue=True or offvalue=False & if(x.get()==YES)

photo = PhotoImage(file='python/images/vs.png')
check_button = Checkbutton(window,text="I do coding",variable=x,onvalue=1,offvalue=0,command=display,
                           font=("Times New Roman",30),bg="black",fg="lightblue",
                           activeforeground="grey",activebackground="black",padx=25,pady=10,image=photo,compound=LEFT)
check_button.pack()

window.mainloop()