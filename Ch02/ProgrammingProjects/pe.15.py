import turtle
import math
turtle.speed(0)
#print(math.sqrt(4**2 + 3**2))

#Beging Drawing One (Two Diamonds)
turtle.penup()
turtle.goto(-200,250)
turtle.pendown()
turtle.fillcolor('green')
turtle.begin_fill()
turtle.right(135)
turtle.forward(70)
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(140)
turtle.right(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(140)
print(turtle.position())

## Begin drawing 22, two triangles.
turtle.penup()
startX = 125
startY = 150
triangle_base = 70
turtle.goto(startX,startY)
turtle.pendown()
turtle.setheading(0)
turtle.forward(triangle_base)
turtle.left(135)
turtle.forward(triangle_base/(math.sqrt(2)))
turtle.left(90)
turtle.forward(triangle_base/(math.sqrt(2)))
turtle.end_fill()
turtle.goto(startX+(triangle_base/2),220)
turtle.goto(195,150)


## Three Dimensial isomorphic view of transparent box
startX = -210
startY = 100
side = 50
turtle.penup()
turtle.goto(startX,startY)
turtle.pendown()
turtle.goto(startX,(startY-side))
turtle.goto((startX+side),(startY-side))
turtle.goto(startX,startY)
turtle.goto(startX,(startY-side))
turtle.goto((startX+side),(startY-side))
turtle.goto((startX+side),startY)
turtle.goto(startX,startY)
turtle.goto((startX+side),(startY-side))
turtle.goto((startX+(2*side)),(startY-side))
turtle.goto((startX+side),startY)
turtle.goto((startX+side),startY-2*side)
turtle.goto(startX,(startY-side))
turtle.goto(startX+side,startY-2*side)
turtle.goto(startX+(2*side),startY-2*side)
turtle.goto(startX+(2*side),(startY-2*side+side))
turtle.goto(startX+(2*side),startY-2*side)
turtle.goto((startX+side),(startY-side))
# five interconnecting circles
turtle.penup()
startX=95
startY=80
side=70
radius=27
turtle.goto(startX,startY)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto((startX+side),startY)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto((startX+side),startY)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto((startX+side+side),startY)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(startX,startY)
turtle.goto((startX+35),(startY-22.5))
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(startX,startY)
turtle.goto((startX+35+side),(startY-22.5))
turtle.pendown()
turtle.circle(radius)
# compass that shows north, south, east, and west 
turtle.penup()
startX = -155
startY = -160
side=65 
radius=15   
turtle.goto(startX,startY) 
turtle.goto((startX-10),(startY+13))
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(startX,startY)
turtle.pendown()
turtle.goto(startX,(startY+side))

turtle.done()