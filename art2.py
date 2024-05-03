import turtle

turtle.bgcolor("#043c4d")

annie = turtle.Turtle()
annie.shape("turtle")
annie.shapesize(2, 2, 12)
annie.color("#f9a778")
annie.width(5)

annie.forward(100)  # Top of square
annie.right(90)
annie.forward(100)  # Right side of square
annie.right(90)
annie.forward(100)  # Bottom of square
annie.right(90)
annie.forward(100)  # Left side of square

anvi = turtle.Turtle()
anvi.shape("turtle")
anvi.width(7)
anvi.color("#78f97e")

anvi.penup()
anvi.goto(0, 100)
anvi.pendown()

anvi.forward(150)
anvi.right(60)
anvi.forward(150)
anvi.right(60)
anvi.forward(150)
anvi.right(60)
anvi.forward(150)
anvi.right(60)
anvi.forward(150)
anvi.right(60)
anvi.forward(150)
anvi.right(60)

dima = turtle.Turtle()
dima.shape("turtle")
dima.width(10)
dima.color("#8a78f9")

dima.penup()
dima.goto(0, -200)
dima.pendown()

dima.forward(200)
dima.left(45)
dima.forward(200)
dima.left(45)
dima.forward(200)
dima.left(45)
dima.forward(200)
dima.left(45)
dima.forward(200)
dima.left(45)
dima.forward(200)
dima.left(45)
dima.forward(200)
dima.left(45)
dima.forward(200)
dima.left(45)

turtle.done()
