import turtle as t
import math as m
import time

window = t.Screen()
window.bgcolor('red')

t.shape("turtle")
t.color("black")
t.pensize(11)
t.speed(5)

def move(x, y):
    t.up()
    t.setposition(x, y)
    t.down

move(-100, -33)

time.sleep(5)
