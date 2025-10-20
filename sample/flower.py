# Цветок из угловатых окружностей

from turtle import *

width(1)    # толщина линии
color('yellow', 'green')  # цвет линии
shape('turtle')     # вид (облик) - черепашка ('arrow' - стрелка)
hideturtle()  # спрятать черепашку
screensize(800, 600, '#000000')
speed(0)   # скорость черепашки

number_circles = 12    # количество окружностей
circle_accuracy = 60    # точность окружности (количество углов правильного многоугольника)
angle_rotation = int(360 / number_circles)    # угол поворота

for i in range(number_circles):
    circle(100, 360, circle_accuracy)
    left(angle_rotation)

done()  # готово
