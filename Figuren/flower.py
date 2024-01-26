import turtle

achtergrondKleur = "lightgreen"
kleurUitlijning = "pink"
kleurVulling = "purple"
snelheid = 10
penGrootte = 10
schaal = 1

turtle.title("BAZ | Snuffeldag Januari 2024 - Bloem")
turtle.bgcolor(achtergrondKleur)

turtle.pen(pencolor=kleurUitlijning, fillcolor=kleurVulling, speed=snelheid, pensize=penGrootte)

wn = turtle.Screen().getcanvas().winfo_toplevel()
wn.wm_attributes("-fullscreen", 1)
wn.wm_attributes("-topmost", 1)

turtle.begin_fill()
for i in range(50):
    turtle.forward(450 * schaal)
    turtle.left(255)

turtle.end_fill()
turtle.hideturtle()
turtle.exitonclick()

# Copyright (c) 2023 Cédric Verlinden & Jasper Verbruggen. All rights reserved.