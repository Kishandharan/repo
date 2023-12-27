import tkinter
from tkinter import ttk
MyTab = tkinter.Tk()
newline = "\n"


def quit1():
    MyTab.destroy()


def a():
    print("a", sep=newline)


def b():
    print("b", sep=newline)


def c():
    print("c", sep=newline)


MyButton1 = ttk.Button(MyTab, text="print a", command=a)
MyButton2 = ttk.Button(MyTab, text="print b", command=b)
MyButton3 = ttk.Button(MyTab, text="print c", command=c)
MyButton4 = ttk.Button(MyTab, text="quit", command=quit1)

MyButton1.pack(ipadx=10, ipady=10)
MyButton2.pack(ipadx=10, ipady=10)
MyButton3.pack(ipadx=10, ipady=10)
MyButton4.pack(ipadx=10, ipady=10)
tkinter.mainloop()
