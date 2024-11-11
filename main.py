from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title="This is an info message box", message="You are a person")
    # while False:
    # messagebox.showwarning(title='Warning', message="You are a virus")
    # messagebox.showerror(title='Error', message="Something went wrong")
    messagebox.askokcancel(title="Ask ok cancel", message="Do you want to do the thing")
window = Tk()

button = Button(window,text="Click me", command=click)
button.pack()

window.mainloop()