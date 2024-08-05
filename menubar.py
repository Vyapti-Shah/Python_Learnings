# menu bar 
from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="OM\\text.txt\\test.txt",title="Open a file",
                                          filetypes=(("text files","*.text"),("all files","*.*")))
    file = open(filepath,'r') #r=read
    print(file.read())
    file.close()
    print(filepath)

def saveFile():
    file = filedialog.asksaveasfile(initialdir="OM\\text.txt\\test.txt",
                                    defaultextension='.txt',
                                    filetypes=[("text files","*.txt"),
                                               ("HTML files","*.html"),
                                               ("JavaScript files","*.js"),
                                               ("Java files","*.java"),
                                               ("Python files","*.py"),
                                               ("All files","*.*")])
    
    if file is None: # if this was not written then the program throws an exception
        return
    
    #filetext = str(text.get(1.0,END))
    filetext = input("Enter some text: ") # used to replace the file
    file.write(filetext)
    file.close()

def cut():
    print("You cut some text")
def copy():
    print("You cut some text")
def paste():
    print("You cut some text")

window = Tk()
window.geometry("500x500")
window.config(background='black')

openImage = PhotoImage(file='python/images/open.png')
saveImage = PhotoImage(file='python/images/save.png')
exitImage = PhotoImage(file='python/images/exit.png')

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("Times New Roman",10)) #tearoff= ----- that comes when the menubar is scrolled down
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile,image=openImage,compound=LEFT)
fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound=LEFT)

editMenu = Menu(menubar,tearoff=0,font=("Times New Roman",10)) #tearoff= ----- that comes when the menubar is scrolled down
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

window.mainloop()