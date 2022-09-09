'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle

g = turtle.Turtle()
g.shape('turtle')

g.color("green")
g.forward(150)
g.backward(300)
g.goto(0,0)
g.goto(37.5,0)
g.begin_fill()
g.color("red")
g.left(90)
g.forward(50)
g.left(90)
g.forward(75)
g.left(90)
g.forward(50)
g.end_fill()
g.penup()
g.color("black")
g.goto(-37.5,50)
g.pendown()
g.begin_fill()
g.right(135)
g.goto(0,70)
g.goto(37.5,50)
g.end_fill()
g.penup()
g.goto(150,0)
g.pendown()
g.color("green")
g.begin_fill()
g.right(60)
g.circle(50,210)
g.end_fill()
g.penup()
g.goto(-150,0)
g.color("grey")
g.right(210)
g.pendown()
g.begin_fill()
g.forward(50)
g.right(140)
g.forward(50)
g.left(150)
g.forward(70)
g.right(150)
g.forward(80)
g.end_fill()
g.penup()
g.goto(-50,140)
g.pendown()
g.begin_fill()
g.color("yellow")
g.circle(40,360)
g.end_fill()
g.goto(50,140)


g.write('Christian Kelly',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
