import turtle
t=turtle.Turtle()
t.home()
t.speed(0)

def outer_layer(radius, segments, color1, color2):
    t.up()
    t.setpos(-20, -radius)
    t.down()
    angle = 360 / segments
    side_length = 2 * 3.14 * radius / segments

    for i in range(segments):
        t.color(color1 if i % 2 == 0 else color2)
        t.begin_fill()
        
        for _ in range(4):
            t.forward(side_length)
            t.left(90)
        
        t.end_fill()
        t.penup()
        t.forward(side_length)
        t.pendown()
        t.left(angle)

def circle(col, rad, val):
    t.up()
    t.setpos(0, val)
    t.down()
    
    t.color(col)
    t.begin_fill()
    t.circle(rad)
    t.end_fill()
    t.up()
     
    t.setpos(0, val)
    t.down()

def diamonds(side_length, nodiamonds, color):
    t.up()
    t.setpos(0,0)
    t.down()
    for i in range(nodiamonds):
        drawdiamond(t, side_length, color)
        t.left(360 / nodiamonds)

def drawdiamond(t, side_length, color):
    t.up()
    t.setpos(0,0)
    t.down()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(side_length)
        t.left(45)
        t.forward(side_length)
        t.left(135)
    t.end_fill()

def petals(radius,nopetals,color):
    angle=360/nopetals
    t.color(color)
    for i in range(nopetals):
        drawpetal(t,radius,angle)
       

def drawpetal(t,radius,angle):
    t.up()
    t.setpos(0,0)
    t.down()
    t.begin_fill()
    t.circle(radius,extent=60)
    t.left(120)
    t.circle(radius,extent=60)
    t.left(180 - angle)
    t.end_fill()

def alternatepetal(radius, petals, color1, color2):
    angle = 360 / petals
    for i in range(petals):
        t.color(color1 if i % 2 == 0 else color2)
        t.begin_fill()
        t.circle(radius, extent=60)
        t.left(120)
        t.circle(radius, extent=60)
        t.left(180 - angle)
        t.end_fill()

def stars(size, nostars, color):
    for i in range(nostars):
        drawstar(t, size, color)
        t.left(360 / nostars)

def drawstar(t, size, color):
    t.up()
    t.setpos(0, 0)
    t.down()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def second_petals(radius,nopetals):
 
    t.color("maroon")
    for i in range(nopetals):
        drawsecondpetal(t,radius)
        t.left(360/nopetals)



def drawsecondpetal(t,radius):
    t.up()
    t.setpos(0,0)
    t.down()
    t.begin_fill()
    t.circle(radius,extent=60)
    t.left(60)
    t.circle(radius,extent=60)
    t.end_fill()

def third_petals(radius,nopetals):
 
    t.color("red")
    for i in range(nopetals):
        drawthirdpetal(t,radius)
        t.left(360/nopetals)

def drawthirdpetal(t,radius):
    t.up()
    t.setpos(0,0)
    t.down()
    t.begin_fill()
    t.circle(radius,extent=33)
    t.left(25)
    t.circle(radius,extent=33)
    t.end_fill()

col = ['orange','white','yellow','maroon','green',]

t.pensize(3)
outer_layer(120*(1+1), 36, col[2], col[3])

t.pensize(1)

circle(col[0], -200, 200)

diamonds(109, 24, col[4])

petals(170,36,col[2])
petals(160,36,col[0])

alternatepetal(150, 36, col[2], col[4])
t.up()
t.goto(0, 0)
t.down()

stars(100, 12, col[3])

petals(70,36,col[1])

circle(col[0], -50, 50)

second_petals(50,6)

circle(col[1], -30, 30)

t.pensize(3)
third_petals(30,8)
t.pensize(1)

t.up()
t.setpos(0,0)
t.down()
circle(col[2], -10, 10)

circle(col[0], -5, 5)

t.hideturtle()



