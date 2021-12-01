import turtle
#move the pen to the top left corner
turtle.penup()
turtle.goto(-50, 50)
turtle.pendown()
#draw the front face of the cube
turtle.goto(50, 50)
turtle.goto(50, -50)
turtle.goto(-50, -50)
turtle.goto(-50, 50)
#make it three-dimensional
turtle.goto(0, 100)
turtle.goto(100, 100)
turtle.goto(100, 0)
turtle.goto(50, -50)
#one more line
turtle.penup()
turtle.goto(50, 50)
turtle.pendown()
turtle.goto(100, 100)
turtle.hideturtle()
turtle.exitonclick()
