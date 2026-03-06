# Программа построения цветка жизни Flower_of_Life, ver. 1.2
# Автор: Качаргин Михаил


import turtle
import math


def petal(x_begin, y_begin, radius, corner, color="black"):
    """
    Построение лепестка из двух дуг
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
    current_pos = turtle.pos()
    turtle.lt(120)
    turtle.circle(radius, 60)
    turtle.lt(120 - corner)
    return current_pos


def flower(x, y, radius, total_places_petals, pattern_num=None, color="black"):
    """
    Построение цветка из лепестков (функция petal).
    Если pattern_num задан, строятся 4 лепестка по шаблону.
    Если pattern_num is None — строятся все лепестки.

    :param x: x - координата центра цветка
    :param y: y - координата центра цветка
    :param radius: радиус цветка
    :param total_places_petals: всего мест лепестков в цветке
    :param pattern_num: номер шаблона (0, 1, 2) для выбора 4 лепестков; если None — все лепестки
    :param color: цвет контура цветка
    :return: кортеж кортежей всех (x, y) координат конца лепестков (внешний круг цветка)
    """
    # Определяем, какие лепестки строить
    if pattern_num is None:
        petal_nums = list(range(1, total_places_petals + 1))  # все лепестки
    else:
        # Логика выбора лепестков по остатку от деления pattern_num на 3
        remainder = pattern_num % 3
        match remainder:
            case 0:
                indices = [0, 1, 3, 4]  # 1, 2, 4, 5
            case 1:
                indices = [0, 2, 3, 5]  # 1, 3, 4, 6
            case 2:
                indices = [1, 2, 4, 5]  # 2, 3, 5, 6
            case _:
                raise ValueError(f"Неподдерживаемый остаток: {remainder}")

        all_petals = list(range(1, total_places_petals + 1))
        petal_nums = [all_petals[i] for i in indices]

    # Проверка корректности количества мест
    if total_places_petals < petal_nums[-1]:
        print("Ошибка в функции flower!")
        print("Количество мест для лепестков должно быть больше или равно номеру последнего лепестка!")
        return None

    petal_ends = []
    angle_step = 360 / total_places_petals  # угол между лепестками

    for num in petal_nums:
        degree = (num - 1) * angle_step  # угол отклонения лепестка
        pet = petal(x, y, radius, degree, color)  # строим лепесток
        petal_ends.append(pet)  # сохраняем координаты конца

    return tuple(petal_ends)  # возвращаем кортеж кортежей


def cir(x, y, radius, color="black"):
    """
    Построение окружности с координатами центра x, y и радиусом radius
    :param x: x - координата центра окружности
    :param y: y - координата центра окружности
    :param radius: радиус окружности
    :param color: цвет контура окружности
    """
    x_set = x
    y_set = y - radius
    turtle.color(color)
    turtle.up()
    turtle.goto(x_set, y_set)
    turtle.down()
    turtle.circle(radius)
    turtle.up()


# Основная программа
turtle.title("Цветок жизни")
turtle.shape('classic')
turtle.setup(600, 600)
turtle.screensize(bg="#777777")
turtle.speed(0)
turtle.hideturtle()
turtle.width(2)

# Настройки построения цветка
radius = 80
total_places_petals = 6
num_flowers = 6
angle_step = int(360 / total_places_petals)

# Построение окружностей — границ
cir(0, 0, 3 * radius)
cir(0, 0, 3.2 * radius)

# Построение лепестков-ограничителей
end = (0, -3 * radius)
for i in range(0, 360, angle_step):
    for _ in range(3):
        end = petal(end[0], end[1], radius, i)

# Построение центрального цветка и лепестков, закрывающих этот цветок
flower_end = flower(0, 0, radius, total_places_petals)  # все лепестки
deg = 60
for x, y in flower_end:
    deg += 60
    petal(x, y, radius, deg)

# Построение 6 цветков по кругу
for degrees in range(0, 360, angle_step):
    x = 2 * radius * math.sin(math.radians(degrees))
    y = 2 * radius * math.cos(math.radians(degrees))
    flower(x, y, radius, total_places_petals)  # все лепестки

# Построение 6 четырёхлистников по кругу
num = -1
for degrees in range(30, 360, angle_step):
    num += 1
    x = 3 ** 0.5 * radius * math.sin(math.radians(degrees))
    y = 3 ** 0.5 * radius * math.cos(math.radians(degrees))
    flower(x, y, radius, total_places_petals, pattern_num=num)  # 4 лепестка по шаблону

print("Построение завершено!")
turtle.done()
