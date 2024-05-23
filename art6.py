import turtle

turtle.bgcolor("LightSkyBlue")

madame_sue = turtle.Turtle()
madame_sue.shape("turtle")
madame_sue.width(6)
madame_sue.speed(0)

madame_sue.color("SaddleBrown")
madame_sue.goto(-50, 0)
madame_sue.goto(0, -500)

madame_sue.color("DeepPink")
madame_sue.penup()
madame_sue.goto(0, 0)
madame_sue.pendown()
madame_sue.begin_fill()
for i in range(72):
    madame_sue.forward(60)
    if i % 2 == 0:
        madame_sue.right(170)
    else:
        madame_sue.left(160)
madame_sue.end_fill()

madame_sue.color("Yellow")
madame_sue.penup()
madame_sue.goto(350, 400)
madame_sue.pendown()
for i in range(50):
    madame_sue.forward(60)
    if i % 2 == 0:
        madame_sue.right(180)
    else:
        madame_sue.left(160)

madame_sue.setheading(85)
madame_sue.penup()
madame_sue.goto(-500, -520)
madame_sue.pendown()
madame_sue.color("DarkGreen")
madame_sue.begin_fill()
for i in range(120):
    madame_sue.forward(100)
    if i % 2 == 0:
        madame_sue.right(170)
    else:
        madame_sue.left(170)
madame_sue.end_fill()

turtle.done()
