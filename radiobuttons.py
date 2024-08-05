# radio buttons - similar to checkbox, but you can choose only one from the group 
from tkinter import *

food = ["pizza","burger","quesadilla"]

def order():
    if(x.get()==0):
        print("You ordered Pizza")
    elif(x.get()==1):
        print("You ordered Burger")
    elif(x.get()==2):
        print("You ordered Quesadilla")
    else:
        print("huh?")

window = Tk()

pizza_image = PhotoImage(file='python/images/pizza.png')
burger_image = PhotoImage(file='python/images/burger.png')
quesadilla_image = PhotoImage(file='python/images/quesadilla.png')
foodPhoto = [pizza_image,burger_image,quesadilla_image]

x = IntVar()

for i in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[i], #adds text to radio buttons
                              variable=x, #groups radiobuttons together if they share the same variables
                              value=i, #assigns each radiobutton a different value
                              padx=25, font=("Times New Roman",0),
                              image=foodPhoto[i], # adds image to radiobuttons
                              compound=LEFT,
                              indicatoron=0, # eliminates circle indicators
                              width=375, command=order)
    radiobutton.pack(anchor=W) # left content 

window.mainloop()