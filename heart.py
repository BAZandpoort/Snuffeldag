import turtle

achtergrondKleur = "lightgreen"
kleurUitlijning = "red"
kleurVulling = "pink"
snelheid = 10
penGrootte = 10

turtle.title("Snuffeldag Februari 2023 - Hartje")
turtle.bgcolor(achtergrondKleur)

turtle.pen(pencolor=kleurUitlijning, fillcolor=kleurVulling, speed=snelheid, pensize=penGrootte)

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