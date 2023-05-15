import turtle

turtle.tracer(0, 0)
turtle.title("BAZ | Snuffeldag Februari 2023 - Voorbeeld")
turtle.bgcolor("black")

turtle.pen(speed=1000)

colors=("white", "pink", "cyan")
for i in range (200):
    turtle.pencolor(colors[i%3])
    turtle.forward(i*4)
    turtle.right(121)

turtle.hideturtle()
turtle.update()
turtle.exitonclick()

# Copyright (c) 2023 Cédric Verlinden & Jasper Verbruggen. All rights reserved.