from tkinter import *
from tkinter.ttk import *
from time import *
label = Label(text="hello")
label.pack()
sleep(3)
label.config(text="bb")
label.pack()
mainloop()
