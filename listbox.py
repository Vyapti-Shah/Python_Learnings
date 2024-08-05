#listbox - A listing of selectable text items within it's own container 

from tkinter import *

def submit():
    #print("You ordered: ")
    #print(listbox.get(listbox.curselection())) #for one selection

    food = []
    for i in listbox.curselection():  #for multiple selection
        food.insert(i,listbox.get(i))
    print("Your order is: ")
    for i in food:
        print(i)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    #listbox.delete(listbox.curselection()) #for one selection
    for i in reversed(listbox.curselection()):  #for multiple selection
        listbox.delete(i)
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,bg="black",fg="white",width=12,font=("Times New Roman",35),selectmode=MULTIPLE)
listbox.pack()
listbox.insert(1,"pizza")
listbox.insert(2,"burger")
listbox.insert(3,"quesadilla")
listbox.insert(4,"soup")
listbox.insert(4,"salad")
listbox.insert(5,"ice cream")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submit_button = Button(window, text="submit", command=submit)
submit_button.pack()

add_button = Button(window, text="add", command=add)
add_button.pack()

delete_button = Button(window, text="delete", command=delete)
delete_button.pack()

window.mainloop()