import turtle

achtergrondKleur = "lightgreen"
kleurUitlijning = "red"
kleurVulling = "pink"
snelheid = 10
penGrootte = 10

turtle.title("BAZ | Snuffeldag Januari 2024 - Hartje")
turtle.bgcolor(achtergrondKleur)

turtle.pen(pencolor=kleurUitlijning, fillcolor=kleurVulling, speed=snelheid, pensize=penGrootte)

wn = turtle.Screen().getcanvas().winfo_toplevel()
wn.wm_attributes("-fullscreen", 1)
wn.wm_attributes("-topmost", 1)

turtle.begin_fill()

turtle.left(50)
turtle.forward(100)
turtle.circle(40, 180)
turtle.left(260)
turtle.circle(40, 180)
turtle.forward(100)

turtle.end_fill()
turtle.hideturtle()
turtle.exitonclick()

# Copyright (c) 2023 Cédric Verlinden & Jasper Verbruggen. All rights reserved.