from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")
root.resizable(0,0)

def time():
    string = strftime('%I:%M:%S  %p')
    label.config(text = string)
    label.after(200 , time)


label = Label(root, font=("ds-digital",35), background = "black" , foreground = "cyan")
label.pack(anchor = 'center')
time()

mainloop()
