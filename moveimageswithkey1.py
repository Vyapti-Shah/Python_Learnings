# move images on a canvas
from tkinter import *

def move_up(event):
    canvas.move(myImage,0,-10)
def move_down(event):
    canvas.move(myImage,0,10)
def move_left(event):
    canvas.move(myImage,-10,0)
def move_right(event):
    canvas.move(myImage,10,0)

window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

canvas = Canvas(window,width=500,height=500)
canvas.pack()

obj_image = PhotoImage(file='python/images/race_car.png')
myImage = canvas.create_image(0,0,image=obj_image,anchor=NW) #NW = north-west

window.mainloop()