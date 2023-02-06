import turtle

turtle.title("Snuffeldag Februari 2023 - Sneeuwvlok")

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


t = turtle.Turtle()
t.color("light_blue", "light_blue") # ONLY CHANGE THESE (outline, fill)
  
t.speed(9999)                    
length = 300.0
  
t.penup()
t.fd(-150)
t.pendown()

t.begin_fill()
for i in range(3):     
    snowflake(t, length, 4) 
    t.right(120) 

t.end_fill()
turtle.mainloop()   