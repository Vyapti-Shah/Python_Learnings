from tkinter import *

def create_window():
    #new_window = Toplevel() #new window on top of the other window that is linked to the bottom window
    new_window = Tk() #new independent window
    window.destroy() #close out of the old window

window = Tk() #bottom window

Button(window,text="create a window",command=create_window).pack()

window.mainloop()