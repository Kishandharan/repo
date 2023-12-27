import tur
turtle.bgcolor("black");
turtle.color("red")
for i in range(100, 0, -10):
    turtle.circle(i)
turtle.color("blue")
turtle.setheading(180)
for i in range(0, 100, 10):
    turtle.circle(i)

