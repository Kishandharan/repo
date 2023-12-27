from tur import *
backGroundcolor = "black"
def function(x,y):
    bgcolor(backGroundcolor)
    color("red")
    circle(80)
    setheading(90)
    up()
    forward(30)
    down()
    setheading(0)
    circle(50)
    setheading(90)
    up()
    forward(20)
    down()
    setheading(0)
    circle(30)
    setheading(270)
    hideturtle()
onscreenclick(function)

