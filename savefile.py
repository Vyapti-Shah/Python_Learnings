# save a file (file dialog)
from tkinter import *
from tkinter import filedialog

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

window = Tk()

button = Button(text="Save",command=saveFile,font=("Times New Roman",20),bg="black",fg="white")
button.pack()

text = Text(window,font=("Times New Roman",20),bg="black",fg="white")
text.pack()

window.mainloop()