from tkinter import *
from tkinter.ttk import *

Window = Tk()


def rbf1():
    print("You ordered burger")


def rbf2():
    print("You ordered pizza")


RadioButton1 = Radiobutton(Window, text="Burger", command=rbf1)
RadioButton2 = Radiobutton(Window, text="Pizza", command=rbf2)
RadioButton1.pack()
RadioButton2.pack()
mainloop()
