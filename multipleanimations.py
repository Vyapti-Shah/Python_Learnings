#multiple animations 
from tkinter import *
import time
from multipleanimationsBall import *

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

voley_ball = Ball(canvas,0,0,100,1,1,"lightblue")
basket_ball = Ball(canvas,0,0,50,2,2,"yellow")
tennis_ball = Ball(canvas,0,0,125,3,3,"orange")

while True:
    voley_ball.move()
    basket_ball.move()
    tennis_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()