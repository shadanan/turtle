import turtle

turtle.bgcolor("#043c4d")

annie = turtle.Turtle()
annie.shape("turtle")
annie.shapesize(2, 2, 12)
annie.color("#f9a778")
annie.width(5)

for count in range(4):
    annie.forward(100)  # Top of square
    annie.right(90)

anvi = turtle.Turtle()
anvi.shape("turtle")
anvi.width(7)
anvi.color("#78f97e")

anvi.penup()
anvi.goto(0, 100)
anvi.pendown()

for count in range(6):
    anvi.forward(150)
    anvi.right(60)

dima = turtle.Turtle()
dima.shape("turtle")
dima.width(10)
dima.color("#8a78f9")

dima.penup()
dima.goto(0, -200)
dima.pendown()

for count in range(8):
    dima.forward(200)
    dima.left(45)

turtle.done()
