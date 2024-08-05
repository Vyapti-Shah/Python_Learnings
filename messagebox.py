from tkinter import * 
from tkinter import messagebox

def click():
    messagebox.showinfo(title='info message box',message='You are a human')

def click1():
    messagebox.showwarning(title='WARNING',message='There is a virus')

def click2():
    messagebox.showerror(title='ERROR',message='something went wrong')

def click3():
    while(True):
        if messagebox.askokcancel(title='Coder',message='Are you a coder?'):
        #if messagebox.askretrycancel(title='Coder',message='Are you a coder?') 
            print("Hello coder")
            break
        else:
            print("Please learn coding")

def click4():
    if messagebox.askyesno(title='Sorry?',message='Are you saying Sorry?'): 
        print("It's Okay!")
    else:
        print("You have to say Sorry!")
        click4()

def click5():
    answer =  messagebox.askquestion(title='Like?',message='Do you like watching Marvel?',icon='error')
    if(answer == 'yes'):
        print("Marvel Fan")
    else:
        print("Not a Marvel Fan")

def click6():
    answers = messagebox.askyesnocancel(title='Yes/No/Cancel',message='Do you like to codel?',icon='warning')
    if(answers==True):
        print("You like to code")
    elif(answers==False):
        print("You don't like to code")
    else:
        print("Cancel")
        
window = Tk()

button = Button(window,text="click if human",command=click)
button.pack()

button1 = Button(window,text="click if virus",command=click1)
button1.pack()

button2 = Button(window,text="click",command=click2)
button2.pack()

button3 = Button(window,text="click me",command=click3)
button3.pack()

button4 = Button(window,text="Respond",command=click4)
button4.pack()

button5 = Button(window,text="Here",command=click5)
button5.pack()

button6 = Button(window,text="Dab",command=click6)
button6.pack()

window.mainloop()