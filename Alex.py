#main file
import turtle
alex = turtle.Turtle()
ali = turtle.Turtle()
bob = turtle.Turtle()
zahra = turtle.Turtle()
alexandra = turtle.Turtle()

from functionfile import*
turtle.colormode(255)
alex.shape("turtle")
ali.shape("turtle")
bob.shape("turtle")
zahra.shape("turtle")
alexandra.shape("turtle")
alex.speed(3)
bob.speed(3)
alexandra.speed(3)
zahra.speed(3)
ali.speed(3)
turtle.bgcolor("black")

sides = 4
angle = 360/sides

r=255
g=255
b=255
myColor=(r,g,b)

r=35
g=70
b=140
my=(r,g,b)

r=50
g=100
b=150
myc=(r,g,b)

r=87
g=112
b=187
myco=(r,g,b)

r=109
g=150
b=200
mycol=(r,g,b)

alex.color(myColor)
move(alex,-350, -300)
polygon(alex,600,sides,myColor)

polygonfill(alex,150,sides,my)
alex.forward(75)
alex.left(45)

polygonfill(alex,105,sides,myc)
alex.forward(50)
alex.left(45)

polygonfill(alex,70,sides,my)

move(alex,250, -300)

polygonfill(alex,150,sides,my)
alex.forward(75)
alex.left(45)

polygonfill(alex,105,sides,myc)
alex.forward(50)
alex.left(45)

polygonfill(alex,70,sides,my)

move(alex,250,300)

polygonfill(alex,150,sides,my)
alex.forward(75)
alex.left(45)

polygonfill(alex,105,sides,myc)
alex.forward(50)
alex.left(45)

polygonfill(alex,70,sides,my)

move(alex,-350, 300)

polygonfill(alex,150,sides,my)
alex.forward(75)
alex.left(45)

polygonfill(alex,105,sides,myc)
alex.forward(50)
alex.left(45)

polygonfill(alex,70,sides,my)

move(alex,-200, -150)

polygonfill(alex,300,sides,my)
alex.forward(150)
alex.left(45)

polygonfill(alex,210,sides,myc)
alex.forward(100)
alex.left(45)

polygonfill(alex,140,sides,my)

move(alex,100, 300)
alex.left(90)

for times in range(4):
    polygonfill(alex,37.5,sides,myco)
    alex.forward(75)
    alex.left(120)
    polygonfill(alex,37.5,3,mycol)
    alex.right(120)

alex.left(90)
alex.forward(37.5)
alex.left(90)
alex.forward(300)
alex.left(180)

for times in range(4):
    polygonfill(alex,37.5,sides,mycol)
    alex.forward(75)
    alex.left(120)
    polygonfill(alex,37.5,3,myco)
    alex.right(120)

alex.left(90)
alex.forward(37.5)
alex.left(90)
alex.forward(300)
alex.left(180)

for times in range(4):
    polygonfill(alex,37.5,sides,myco)
    alex.forward(75)
    alex.left(120)
    polygonfill(alex,37.5,3,mycol)
    alex.right(120)

alex.left(90)
alex.forward(37.5)
alex.left(90)
alex.forward(300)
alex.left(180)

for times in range(4):
    polygonfill(alex,37.5,sides,mycol)
    alex.forward(75)
    alex.left(120)
    polygonfill(alex,37.5,3,myco)
    alex.right(120)
move(alex,-350, 150)
alex.left(90)

for times in range(4):
    polygonfill(alex,37.5,sides,myco)
    alex.forward(75)
    alex.left(120)
    polygonfill(alex,37.5,3,mycol)
    alex.right(120)

alex.left(90)
alex.forward(37.5)
alex.left(90)
alex.forward(300)
alex.left(180)

for times in range(4):
    polygonfill(alex,37.5,sides,mycol)
    alex.forward(75)
    alex.left(120)
    polygonfill(alex,37.5,3,myco)
    alex.right(120)

alex.left(90)
alex.forward(37.5)
alex.left(90)
alex.forward(300)
alex.left(180)

for times in range(4):
    polygonfill(alex,37.5,sides,myco)
    alex.forward(75)
    alex.left(120)
    polygonfill(alex,37.5,3,mycol)
    alex.right(120)

alex.left(90)
alex.forward(37.5)
alex.left(90)
alex.forward(300)
alex.left(180)

for times in range(4):
    polygonfill(alex,37.5,sides,mycol)
    alex.forward(75)
    alex.left(120)
    polygonfill(alex,37.5,3,myco)
    alex.right(120)

move(alex,-200, -300)
alex.left(90)

for times in range(4):
    polygonfill(alex,37.5,sides,myco)
    alex.forward(75)
    alex.left(120)
    polygonfill(alex,37.5,3,mycol)
    alex.right(120)

alex.left(90)
alex.forward(37.5)
alex.left(90)
alex.forward(300)
alex.left(180)

for times in range(4):
    polygonfill(alex,37.5,sides,mycol)
    alex.forward(75)
    alex.left(120)
    polygonfill(alex,37.5,3,myco)
    alex.right(120)

alex.left(90)
alex.forward(37.5)
alex.left(90)
alex.forward(300)
alex.left(180)

for times in range(4):
    polygonfill(alex,37.5,sides,myco)
    alex.forward(75)
    alex.left(120)
    polygonfill(alex,37.5,3,mycol)
    alex.right(120)

alex.left(90)
alex.forward(37.5)
alex.left(90)
alex.forward(300)
alex.left(180)

for times in range(4):
    polygonfill(alex,37.5,sides,mycol)
    alex.forward(75)
    alex.left(120)
    polygonfill(alex,37.5,3,myco)
    alex.right(120)
move(alex,250, -150)
alex.left(90)

for times in range(4):
    polygonfill(alex,37.5,sides,myco)
    alex.forward(75)
    alex.left(120)
    polygonfill(alex,37.5,3,mycol)
    alex.right(120)

alex.left(90)
alex.forward(37.5)
alex.left(90)
alex.forward(300)
alex.left(180)

for times in range(4):
    polygonfill(alex,37.5,sides,mycol)
    alex.forward(75)
    alex.left(120)
    polygonfill(alex,37.5,3,myco)
    alex.right(120)

alex.left(90)
alex.forward(37.5)
alex.left(90)
alex.forward(300)
alex.left(180)

for times in range(4):
    polygonfill(alex,37.5,sides,myco)
    alex.forward(75)
    alex.left(120)
    polygonfill(alex,37.5,3,mycol)
    alex.right(120)

alex.left(90)
alex.forward(37.5)
alex.left(90)
alex.forward(300)
alex.left(180)

for times in range(4):
    polygonfill(alex,37.5,sides,mycol)
    alex.forward(75)
    alex.left(120)
    polygonfill(alex,37.5,3,myco)
    alex.right(120)
move(alex,-50, 0)
fancyspiral(alex,4,myColor)

move(alexandra,-275, -225)
sfancyspiral(alexandra,2,myColor)

move(zahra,175, -225)
sfancyspiral(zahra,2,myColor)

move(ali,-275, 225)
sfancyspiral(ali,2,myColor)

move(bob,175, 225)
sfancyspiral(bob,2,myColor)

turtle.done()
