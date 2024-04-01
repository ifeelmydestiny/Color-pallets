import turtle as t
from turtle import Turtle, Screen
import random

timmy = Turtle()
t.colormode(255)
colors = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]



y = -270
timmy.hideturtle()

for j in range(10):
    timmy.speed("fastest")
    timmy.penup()
    y += 50
    timmy.goto(-250,y)
    for i in range(10):
        timmy.pendown()
        timmy.color(random.choice(colors))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)



















screen = Screen()
screen.exitonclick()