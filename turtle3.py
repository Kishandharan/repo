from tur import *
from random import randint
bg_colors = ["black","red","blue","white"]
pencolor("red")
bgcolor("black")
hideturtle()
def func(col):
    fillcolor(col)
    begin_fill()
    circle(90)
    end_fill()
def changeColor(v,p):
    global bg_colors
    ind = randint(0, len(bg_colors)-1)
    color = bg_colors[ind]
    bgcolor(color)
onscreenclick(changeColor)
func("red")
forward(30)
func("yellow")
forward(30)
func("green")
forward(30)
func("purple")
