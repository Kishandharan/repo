from tkinter import *
from tkinter.ttk import *
from random import *
window = Tk()
number = 0
def one():
    global number
    number = 1
button = Button(window, text="One", command=one)
print(number)
button.pack(ipadx=5, ipady=5)
mainloop()