import turtle

# Setting up my Snowman Turtle
window = turtle.Screen()
snowman = turtle.Turtle()
snowman.speed(15)
snowman.width(3)
snowman.color("black")

# Body of the snowman
snowman.penup()
snowman.goto(0,300)
snowman.pendown()
snowman.circle(80)

snowman.penup()
snowman.goto(0,80)
snowman.pendown()
snowman.circle(110)

snowman.penup()
snowman.goto(0,-200)
snowman.pendown()
snowman.circle(140)

# Eyes
snowman.penup()
snowman.goto(-30,390)
snowman.pendown()
snowman.begin_fill()
snowman.circle(10)
snowman.end_fill()

snowman.penup()
snowman.goto(30,390)
snowman.pendown()
snowman.begin_fill()
snowman.circle(10)
snowman.end_fill()

# Mouth
snowman.penup()
snowman.goto(0,360)
snowman.pendown()
snowman.forward(40)
snowman.backward(80)
snowman.left(270)
snowman.begin_fill()
snowman.circle(40,180)
snowman.end_fill()

# Top Hat
snowman.penup()
snowman.goto(70,460)
snowman.pendown()
snowman.right(90)
snowman.begin_fill()
snowman.backward(140)
snowman.right(90)
snowman.forward(10)
snowman.left(90)
snowman.forward(140)
snowman.left(90)
snowman.forward(10)
snowman.end_fill()

snowman.left(90)
snowman.forward(120)
snowman.right(90)
snowman.color("red")
snowman.begin_fill()
snowman.forward(75)
snowman.right(90)
snowman.forward(100)
snowman.right(90)
snowman.forward(75)
snowman.end_fill()

# Buttons
snowman.penup()
snowman.goto(0,130)
snowman.pendown()
snowman.color("blue")
snowman.begin_fill()
snowman.circle(5)
snowman.end_fill()

snowman.penup()
snowman.goto(0,185)
snowman.pendown()
snowman.begin_fill()
snowman.circle(5)
snowman.end_fill()

snowman.penup()
snowman.goto(0,240)
snowman.pendown()
snowman.begin_fill()
snowman.circle(5)
snowman.end_fill()

# Arms and Hands
snowman.penup()
snowman.goto(109,210)
snowman.pendown()
snowman.color("black")
snowman.left(120)
snowman.forward(160)

snowman.left(60)
snowman.forward(40)
snowman.backward(40)
snowman.right(50)
snowman.forward(40)
snowman.backward(40)
snowman.right(50)
snowman.forward(40)

snowman.penup()
snowman.goto(-109,210)
snowman.pendown()
snowman.left(140)
snowman.forward(160)

snowman.left(60)
snowman.forward(40)
snowman.backward(40)
snowman.right(50)
snowman.forward(40)
snowman.backward(40)
snowman.right(50)
snowman.forward(40)



turtle.done()