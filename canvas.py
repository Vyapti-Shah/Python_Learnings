#canvas - widget that is used to draw graphs, plot, image in a window

from tkinter import * 

window = Tk()

canvas = Canvas(window,height=500,width=500)
canvas.create_line(0,0,500,500,fill="blue",width=2) #starting(x,y)=(0,0) #ending(x,y)=(500,500)
canvas.create_line(0,500,500,0,fill="red",width=2) 
canvas.create_rectangle(50,50,250,250,fill="lightblue") 
points = [250,0,500,500,0,500] #starting(x,y)=(0,0) #left side(x,y)=(500,500) #right side(x,y)=(0,500)
canvas.create_polygon(points,fill="yellow",outline="black",width=2) 
canvas.create_arc(0,0,500,500,fill="pink") 
canvas.create_arc(0,0,500,500,fill="grey",style=CHORD,start=180) 
canvas.create_arc(0,0,500,500,fill="grey",style=ARC,start=90) 
canvas.create_arc(0,0,500,500,fill="grey",style=ARC,start=270,extent=180) 

canvas.pack()

window.mainloop()