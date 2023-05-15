import turtle

achtergrondKleur = "lightgreen"
kleurUitlijning = "pink"
kleurVulling = "purple"
snelheid = 10
penGrootte = 10

turtle.title("BAZ | Snuffeldag Februari 2023 - Bloem")
turtle.bgcolor(achtergrondKleur)

turtle.pen(pencolor=kleurUitlijning, fillcolor=kleurVulling, speed=snelheid, pensize=penGrootte)

turtle.begin_fill()
for i in range(50):
    turtle.forward(300)
    turtle.left(170)

turtle.end_fill()
turtle.hideturtle()
turtle.exitonclick()

# Copyright (c) 2023 Cédric Verlinden & Jasper Verbruggen. All rights reserved.