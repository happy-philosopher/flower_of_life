# Программа построения цветка жизни - Flower of Life, ver. 1.1
# Автор: Качаргин Михаил
# ToDo: Нужно объединить функции get_selected_petals и flower


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


def flower(x, y, radius, total_places_petals, petal_nums = [1, 2, 3, 4, 5, 6], color="black"):
    """
        Построение цветка flower из лепестков (функция petal), можно построить любые лепестки
        в любом месте цветка и какие-то пропустить
        :param x: x - координата центра цветка
        :param y: y - координата центра цветка
        :param radius: радиус цветка
        :param total_places_petals: всего мест лепестков в цветке
        :param petal_nums: кортеж нужных номеров лепестков в цветке
        :param color: цвет контура цветка
        :return: кортеж кортежей всех (x, y) координат конца лепестков (внешний круг цветка)
    """
    if total_places_petals >= petal_nums[-1]:  # проверка количества мест для лепестков и номера последнего лепестка
        petal_ends = []
        angle_step = 360 / total_places_petals  # угол, через который шагаем для построения лепестка
        for i in range(len(petal_nums)):  # построение цветка: только те лепестки, которые указаны в кортеже petal_nums
            degree = (petal_nums[i] - 1) * angle_step  # угол отклонения лепестка
            pet = petal(x, y, radius, degree, color)  # координаты (x,y) конца лепестка и построение лепестка
            petal_ends.append(pet)  # добавление в список координат (x,y) конца лепестка
        petal_ends = tuple(petal_ends)
        return petal_ends  # возврат кортежа кортежей всех (x,y) координат конца лепестков (внешний круг цветка)
    else:
        print("Ошибка в функции flower!")
        print("Количество мест для лепестков должно быть больше или равно количеству лепестков!")
        return None


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


def get_selected_petals(num_petal, total_petals):
    """

        :param num_petal:
        :param total_petals:
        :return:
    """
    selected_petals = []
    for i in range(1, total_petals + 1):  # заполняем список порядковыми номерами лепестков цветка
        selected_petals.append(i)
    remainder = num_petal % 3  # в зависимости от номера выбираем расположение лепестков в цветке
    match remainder:
        case 0:
            indices = [0, 1, 3, 4]  # 1, 2, 4, 5
        case 1:
            indices = [0, 2, 3, 5]  # 1, 3, 4, 6
        case 2:
            indices = [1, 2, 4, 5]  # 2, 3, 5, 6
        case _:
            raise ValueError(f"Неподдерживаемый остаток: {remainder}")
    return [selected_petals[i] for i in indices]


# Основная программа
# Настройки черепашки и окна
turtle.title("Цветок жизни")
turtle.shape('classic')  # вид (облик) - черепашка ('turtle' - черепашка, 'arrow' - стрелка)
turtle.setup(600, 600)  # размер окна для вывода графики
turtle.screensize(bg ="#777777")  # цвет фона
turtle.speed(0)  # скорость черепашки
turtle.hideturtle()  # спрятать черепашку
turtle.width(2)      # толщина линии

# Настройки построения цветка
radius = 80  # Радиус цветка
total_places_petals = 6  # Количество мест лепестков в цветке
num_flowers = 6  # Количество цветков по кругу
angle_step = int(360 / total_places_petals)  # угол, через который шагаем для построения лепестка или цветка

# Построение окружностей - границ
cir(0, 0, 3 * radius)
cir(0, 0, 3.2 * radius)

# Построение лепестков ограничителей
end = (0, -3 * radius)
for i in range(0, 360, angle_step):
    for _ in range(3):
        end = petal(end[0], end[1], radius, i)

# Построение центрального цветка и лепестков, закрывающих этот цветок
flower_end = flower(0, 0, radius, total_places_petals)  # 0 - центр
deg = 60
for x, y in flower_end:
    deg += 60
    petal(x, y, radius, deg)

# Построение 6-ти цветков по кругу (центры в 3)
for degrees in range(0, 360, angle_step):
    x = 2 * radius * math.sin(math.radians(degrees))
    y = 2 * radius * math.cos(math.radians(degrees))
    flower(x, y, radius, total_places_petals)

# Построение 6-ти четырёхлистников по кругу (центры в 2)
num = -1
for degrees in range(30, 360, angle_step):
    num += 1
    x = 3**0.5 * radius * math.sin(math.radians(degrees))
    y = 3**0.5 * radius * math.cos(math.radians(degrees))
    selected_petals = get_selected_petals(num, total_places_petals)
    flower(x, y, radius, total_places_petals, selected_petals)

print("Построение завершено!")
turtle.done()
