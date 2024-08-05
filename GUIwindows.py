from tkinter import *

# widgets - GUI elements : buttons, textboxes, labels, images 
# windows - serves as a container to hold or contain these widgets 

window = Tk() #instantiates an instance of a window 
window.geometry("500x500") # x = ex 
window.title("Vyapti Shah")

icon = PhotoImage(file='python/images/vs.png')
window.iconphoto(True,icon)

window.config(background='black')

window.mainloop() #place window on computer screen & listens for events