import turtle

turtle.title("Snuffeldag Februari 2023 - Voorbeeld")
turtle.bgcolor("black")

t = turtle.Turtle()
t.pen(speed=30)
t.shape("circle")

col=("white", "pink", "cyan")
for i in range (200):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(121)
    
turtle.mainloop()