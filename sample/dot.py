# Программа "Проба точки - dot"

import random
import turtle

turtle.title("Много точек")
turtle.shape('classic')  # вид (облик) - черепашка ('turtle' - черепашка, 'arrow' - стрелка)
turtle.setup(800, 600)  # размер окна для вывода графики
turtle.screensize(750, 550, '#000025')  # размер экрана для рисования
turtle.speed(0)  # скорость черепашки
turtle.hideturtle()  # спрятать черепашку

num_points = 100  # количество точек
dia_begin = 2  # диаметр точки начала диапазона
dia_end = 150  # диаметр точки конца диапазона

r_begin = 0  # начало диапазона красного цвета (0..255)
r_end = 255  # конец диапазона красного цвета (0..255)

g_begin = 0  # начало диапазона зелёного цвета (0..255)
g_end = 255  # конец диапазона зелёного цвета (0..255)

b_begin = 200  # начало диапазона синего цвета (0..255)
b_end = 25  # конец диапазона синего цвета (0..255)

# Защита диапазонов от "дурака"
if dia_begin > dia_end:
    dia_begin, dia_end = dia_end, dia_begin
if r_begin > r_end:
    r_begin, r_end = r_end, r_begin
if g_begin > g_end:
    g_begin, g_end = g_end, g_begin
if b_begin > b_end:
    b_begin, b_end = b_end, b_begin

# Основной цикл рисования точек-кружочек
for i in range(num_points):
    x = random.randint(-600, 600)
    y = random.randint(-500, 500)
    diameter = random.randint(dia_begin, dia_end)
    R = hex(random.randint(r_begin, r_end))[2:]
    if len(R) < 2:
        R = "0" + R
    G = hex(random.randint(g_begin, g_end))[2:]
    if len(G) < 2:
        G = "0" + G
    B = hex(random.randint(b_begin, b_end))[2:]
    if len(B) < 2:
        B = "0" + B
    color = "#" + R + G + B
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(diameter, color)

turtle.done()
