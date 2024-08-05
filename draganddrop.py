# drag and drop
from tkinter import * 

def drag_start(event):
    both_label = event.widget 
    both_label.startX = event.x
    both_label.startY = event.y

def drag_motion(event):
    both_label = event.widget 
    x = both_label.winfo_x() - both_label.startX + event.x #label.winfo_x() = gets the top left x coordinate 
                                                 #label.startX = place where we click the label 
                                                 #event.x = place where we began dragging the label
    y = both_label.winfo_y() - both_label.startY + event.y #label.winfo_y() = gets the top left y coordinate
                                                 #label.startY = place where we click the label 
                                                 #event.y = place where we began dragging the label
    both_label.place(x=x,y=y)

window = Tk()

label = Label(window,bg="lightblue",width=10,height=5)
label.place(x=0,y=0)

label0 = Label(window,bg="pink",width=10,height=5)
label0.place(x=100,y=100)

label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion) #to get the motion done by clicking left side of mouse 

label0.bind("<Button-1>",drag_start)
label0.bind("<B1-Motion>",drag_motion)

window.mainloop()