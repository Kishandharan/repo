from tkinter import *
import os
print(os.getcwd())
window = Tk()
window.title("Simple typing area")
text = Text(width="300", height="700", font=("Consolas", 19))
text.config(bg = "#090170")
text.config(fg = "orange")
text.config(insertbackground = "orange")
text.pack()
window.mainloop()
