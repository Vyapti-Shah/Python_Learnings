# open a file (file dialog) 
from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="OM\\text.txt\\test.txt",title="Open a file",
                                          filetypes=(("text files","*.text"),("all files","*.*")))
    file = open(filepath,'r') #r=read
    print(file.read())
    file.close()
    print(filepath)
    # for output open OM/text.txt/test.txt

window = Tk()

button = Button(text="Open",command=openFile,font=("Times New Roman",20),bg="black",fg="white")
button.pack()

window.mainloop()