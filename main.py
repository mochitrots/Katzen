import turtle as t
import math as m

window = t.Screen()
window.bgcolor("red")

cursor = t.Turtle()

cursor.shape("turtle")
cursor.color("black")
cursor.speed(3)
cursor.pensize(10)

def move(cursor, x, y):
    cursor.penup()
    cursor.setposition(x, y)
    cursor.pendown()

def movex(cursor, x):
    cursor.penup()
    cursor.setx(x)
    cursor.pendown()

def movey(cursor, y):
    cursor.penup()
    cursor.sety(y)
    cursor.pendown()

# Position along circle
def posc(x, y, radius, angle):
    radians = m.radians(angle)
    return [x + (radius * m.sin(radians)), y + (radius * m.cos(radians))]

movey(cursor, -150)
cursor.circle(150)

noseoffset = -15

movey(cursor, -20 + noseoffset)
cursor.circle(20)

move(cursor, -100, -20 + noseoffset)
cursor.right(90)
cursor.circle(50, 180)
cursor.left(180)
cursor.circle(50, 180)

eyespacingx = 30
eyeposy = 40
eyeradius = 30

#Right eye
move(cursor, eyespacingx, eyeposy)
cursor.right(180)
cursor.circle(eyeradius, -180)

#Left eye
move(cursor, -eyespacingx, eyeposy)
cursor.circle(eyeradius, 180)

move(cursor, -20, -60 + noseoffset)
cursor.circle(20, 180)

#Right ear
earangle = 25
earsize = 85
earwidth = 22

pos1 = posc(0, 0, 150, earangle)
move(cursor, pos1[0], pos1[1])

pos2 = posc(0, 0, 150 + earsize, earangle + earwidth)
cursor.setposition(pos2[0], pos2[1])

pos3 = posc(0, 0, 150, earangle + earwidth * 2)
cursor.setposition(pos3[0], pos3[1])

#Left ear
pos4 = posc(0, 0, 150, -earangle)
move(cursor, pos4[0], pos4[1])

pos5 = posc(0, 0, 150 + earsize, -earangle -earwidth)
cursor.setposition(pos5[0], pos5[1])

pos6 = posc(0, 0, 150, -earangle -earwidth * 2)
cursor.setposition(pos6[0], pos6[1])

lenwhisker = 180

# Right whisker
move(cursor, 50, -15)
cursor.setheading(0)
cursor.fd(lenwhisker)

move(cursor, 50, 0)
cursor.left(5)
cursor.fd(lenwhisker)

# Left whisker

move(cursor, -50, -15)
cursor.setheading(180)
cursor.fd(lenwhisker)

move(cursor, -50, 0)
cursor.right(5)
cursor.fd(lenwhisker)

window.exitonclick()