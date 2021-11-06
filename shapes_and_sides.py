import random
import time
from turtle import *
color("cyan")
shape("classic")
shapesize(2.5)
pensize(5)
speed(10)
shapes = random.randint(1, 100)
sides = random.randint(1, 20)
print(shapes, sides)
print(shapes*sides)
print(shapes/sides)
for x in range(shapes):
    for y in range(sides):
        forward(50)
        right(360/sides)
        color(random.random(), random.random(), random.random())
    right(360/shapes)
time.sleep(10)