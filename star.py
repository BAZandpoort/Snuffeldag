import turtle

turtle.title("Snuffeldag Februari 2023 - Ster")
turtle.bgcolor("#83b011") # ONLY CHANGE THESE

t = turtle.Turtle()
t.pen(pencolor="white", fillcolor="purple", pensize=10, speed=5) # ONLY CHANGE THESE
t.shape("circle") # ONLY CHANGE THESE (square, arrow, circle, triangle)

t.begin_fill()
for i in range(8):
    t.forward(200)
    t.left(135)

t.end_fill()
turtle.mainloop()