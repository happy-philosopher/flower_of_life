import turtle
import math


def petal(x_begin, y_begin, radius, corner, color):
    """
        Рисование лепестка из двух дуг
        :param x_begin: x - координата начала лепестка
        :param y_begin: y - координата начала лепестка
        :param radius: радиус дуги
        :param corner: угол наклона лепестка
        :param color: цвет контура лепестка
    """
    turtle.color(color)
    turtle.up()
    turtle.goto(x_begin, y_begin)
    turtle.down()
    turtle.lt(corner)
    turtle.circle(radius, 60)
    turtle.lt(120)
    turtle.circle(radius, 60)
    turtle.lt(120 - corner)


turtle.title("Цветок жизни")
turtle.shape('classic')  # вид (облик) - черепашка ('turtle' - черепашка, 'arrow' - стрелка)
width_setup = 800
hight_setup = 600
turtle.setup(width_setup, hight_setup)  # размер окна для вывода графики
turtle.screensize(750, 550, '#AAAAAA')  # размер экрана для рисования
turtle.speed(0)  # скорость черепашки
#turtle.hideturtle()  # спрятать черепашку
turtle.width(2)

# Начало построения
radius = 80  # Радиус цветка
num_flowers = 6  # Количество цветков по кругу
total_places_petals = 6  # Количество мест для лепестков в цветке


# 6 цветков по кругу
# Луч 30 градусов
selected_petals = [1, 2, 4, 5]  # Номера лепестков (1–6)
for petal_num in selected_petals:
    deg = (petal_num - 1) * 360 / total_places_petals
    print(deg)
    petal(1.5 * radius * math.tan(math.radians(30)), 1.5 * radius, radius, deg, "green")
print()

# Луч 90 градусов
selected_petals = [1, 3, 4, 6]  # Номера лепестков (1–6)
for petal_num in selected_petals:
    deg = (petal_num - 1) * 360 / total_places_petals  # Угол = (номер − 1) × 60°
    print(deg)
    petal(1.5 * radius / math.cos(math.radians(30)), 0, radius, deg, "green")
print()

# Луч 150 градусов
selected_petals = [2, 3, 5, 6]  # Номера лепестков (1–6)
for petal_num in selected_petals:
    deg = (petal_num - 1) * 360 / total_places_petals  # Угол = (номер − 1) × 60°
    print(deg)
    petal(1.5 * radius * math.tan(math.radians(30)), -1.5 * radius, radius, deg, "green")
print()

# Луч 210 градусов
selected_petals = [1, 2, 4, 5]  # Номера лепестков (1–6)
for petal_num in selected_petals:
    deg = (petal_num - 1) * 360 / total_places_petals  # Угол = (номер − 1) × 60°
    print(deg)
    petal(-1.5 * radius * math.tan(math.radians(30)), -1.5 * radius, radius, deg, "green")
print()

# Луч 270 градусов
selected_petals = [1, 3, 4, 6]  # Номера лепестков (1–6)
for petal_num in selected_petals:
    deg = (petal_num - 1) * 360 / total_places_petals  # Угол = (номер − 1) × 60°
    print(deg)
    petal(-1.5 * radius / math.cos(math.radians(30)), 0, radius, deg, "green")
print()

# Луч 330 градусов
selected_petals = [2, 3, 5, 6]  # Номера лепестков (1–6)
for petal_num in selected_petals:
    deg = (petal_num - 1) * 360 / total_places_petals  # Угол = (номер − 1) × 60°
    print(deg)
    petal(-1.5 * radius * math.tan(math.radians(30)), 1.5 * radius, radius, deg, "green")


turtle.done()
