import turtle

achtergrondKleur = "black"
kleurenUitlijning = ("lime", "darkgreen", "white", "lime", "darkgreen")
penGrootte = 10

turtle.tracer(0, 0)
turtle.title("BAZ | Snuffeldag Januari 2024 - Voorbeeld")
turtle.bgcolor(achtergrondKleur)

wn = turtle.Screen().getcanvas().winfo_toplevel()
wn.wm_attributes("-fullscreen", 1)
wn.wm_attributes("-topmost", 1)

for i in range (200):
    turtle.pencolor(kleurenUitlijning[i%4])
    turtle.forward(i*4)
    turtle.right(121)

turtle.hideturtle()
turtle.update()
turtle.exitonclick()

# Copyright (c) 2023 Cédric Verlinden & Jasper Verbruggen. All rights reserved.