import turtle

turtle.bgcolor("#043c4d")

keith = turtle.Turtle()
keith.shape("turtle")
keith.width(5)
keith.color("#7ef582")

for distance in range(4, 500, 4):
    keith.forward(distance)
    keith.right(60)

turtle.done()
