import turtle

achtergrondKleur = "lightgreen"
kleurUitlijning = "white"
kleurVulling = "purple"
snelheid = 10
penGrootte = 10

turtle.title("Snuffeldag Februari 2023 - Ster")
turtle.bgcolor(achtergrondKleur)

turtle.pen(pencolor=kleurUitlijning, fillcolor=kleurVulling, speed=snelheid, pensize=penGrootte)

turtle.begin_fill()
for i in range(8):
    turtle.forward(200)
    turtle.left(135)

turtle.end_fill()
turtle.hideturtle()
turtle.exitonclick()