import math
import turtle

turtle.shape("turtle")
turtle.setup(width=900, height=700)
turtle.speed(0)
turtle.bgcolor('black')
turtle.color('red')



def heart1(h):
    return 15 * math.sin(h) ** 3

def heart2(h):
    return 12 * math.cos(h) - 5 * math.cos(2 * h) - 2 * math.cos(3 * h) - math.cos(4 * h)


turtle.penup()
turtle.goto(heart1(0) * 20, heart2(0) * 20)
turtle.pendown()

for i in range(400):
    x, y = heart1(i) * 20, heart2(i) * 20
    turtle.goto(x, y)


turtle.penup()
turtle.goto(0, 35)
turtle.pendown()
turtle.write("[ENTER YOUR FELLINGS ]", align='center', font=('Arial', 30, 'bold'))


turtle.penup()
turtle.goto(heart1(0) * 20, heart2(0) * 20 - 100)
turtle.pendown()


for i in range(300):
    x, y = heart1(i) * 10, heart2(i) * 10 - 100
    turtle.goto(x, y)


turtle.penup()
turtle.goto(heart1(0) * 20, heart2(0) * 20 - 150)
turtle.pendown()

for i in range(200):
    x, y = heart1(i) * 5, heart2(i) * 5 - 150
    turtle.goto(x, y)


turtle.penup()
turtle.goto(heart1(0) * 20, heart2(0) * 20 - 180)
turtle.pendown()
for i in range(150):
    x, y = heart1(i) * 2, heart2(i) * 2 - 180
    turtle.goto(x, y)


turtle.penup()
turtle.goto(0, 243)
turtle.pendown()
turtle.write("WHAT YOU WANT ", align='center', font=('Arial', 40, 'bold'))

turtle.done()