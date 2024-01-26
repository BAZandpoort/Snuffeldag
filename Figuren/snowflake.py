import turtle

achtergrondKleur = "lightgreen"
kleurUitlijning = "lightblue"
kleurVulling = "aqua"
snelheid = 100
penGrootte = 2

turtle.title("BAZ | Snuffeldag Februari 2023 - Sneeuwvlokje")
turtle.bgcolor(achtergrondKleur)

def snowflake(t, lengthSide, levels): 
    if levels == 0: 
        t.forward(lengthSide) 
        return

    lengthSide /= 3.0
    snowflake(t, lengthSide, levels-1) 
    t.left(60) 
    snowflake(t, lengthSide, levels-1) 
    t.right(120) 
    snowflake(t, lengthSide, levels-1) 
    t.left(60) 
    snowflake(t, lengthSide, levels-1) 


turtle.pen(pencolor=kleurUitlijning, fillcolor=kleurVulling, speed=snelheid, pensize=penGrootte)
                  
length = 300.0
  
turtle.penup()
turtle.fd(-150)
turtle.pendown()

turtle.begin_fill()
for i in range(3):
    snowflake(turtle, length, 4) 
    turtle.right(120) 

turtle.end_fill()
turtle.hideturtle()
turtle.exitonclick()

# Copyright (c) 2023 Cédric Verlinden & Jasper Verbruggen. All rights reserved.