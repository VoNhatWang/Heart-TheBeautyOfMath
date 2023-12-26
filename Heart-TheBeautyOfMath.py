from turtle import Screen, Turtle, ontimer
from math import sin, cos
from time import perf_counter

screen = Screen()
screen.title("Optimized by Võ Nhật Quang")
screen.bgcolor(0, 0, 0)
screen.setup(500, 500)
screen.tracer(0)

t = perf_counter()

def ve_dau_cham(turtle, x, y, size, color):
    turtle.goto(x, y)
    turtle.dot(size, color)

def tao_toa_do(t, i):
    x = sin(2 - 0.2 * sin(3 * t + i / 20) ** 8 + i / 2)
    x *= 200 * cos(i)
    y = 200 * sin(i + 0.7 ** cos(i) ** 0.05) - 30
    return x, y

def cap_nhat_dau_cham():
    turtle.clear()
    global t
    t = perf_counter()
    for i in range(500):
        if cos(i) < 0:
            continue
        x, y = tao_toa_do(t, i)
        dot_size = 20
        dot_color = (1, 0, sin(i + t + sin(t / 2)) / 2 + 0.5)
        ve_dau_cham(turtle, x, y, dot_size, dot_color)
    screen.update()
    screen.ontimer(cap_nhat_dau_cham, 10)

turtle = Turtle()
turtle.hideturtle()
turtle.penup()

cap_nhat_dau_cham()
screen.mainloop()
