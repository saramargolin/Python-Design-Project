#function file

def polygon(T,distance,sides,c):
    angle=360/sides
    T.color(c)
    for times in range(sides):
        T.forward(distance)
        T.left(angle)

def polygonfill(T,distance,sides,c):
    angle=360/sides
    T.begin_fill()
    T.color(c)
    for times in range(sides):
        T.forward(distance)
        T.left(angle)
    T.end_fill()

def move(T,x, y):
    T.penup()
    T.goto(x, y)
    T.pendown()

def star(T,distance,c):
    T.color(c)
    for times in range(5):
        T.forward(distance)
        T.left(216)
        
def fancyspiral(T,distance,c):
    T.color(c)
    for times in range(136):
        T.forward(distance)
        T.left(90.5)
        distance+=1

def sfancyspiral(T,distance,c):
    T.color(c)
    for times in range(68):
        T.forward(distance)
        T.left(90.5)
        distance+=1
