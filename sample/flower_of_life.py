import turtle
import math

# Создаем окно для рисования
window = turtle.Screen()
window.bgcolor("white")

# Создаем черепаху для рисования
t = turtle.Turtle()
t.speed(0)

# Радиус окружности А
radius_a = 100

# Начальная точка окружности А
start_point_a = (0, -radius_a)

# Рисуем окружность А
t.penup()
t.goto(start_point_a)
t.pendown()
t.circle(radius_a)

# Рисуем 6 дополнительных окружностей на окружности А
num_circles = 6
angle = 360 / num_circles
radius_b = radius_a

for i in range(num_circles):
    # Вычисляем положение следующей окружности
    x = start_point_a[0] + radius_b * math.sin(math.radians(angle * i))
    y = start_point_a[1] + radius_b * math.cos(math.radians(angle * i))
    print(f"x{i} = ({round(x,1)}; {round(y,1)})")
    i5 = i

    # Рисуем следующую окружность
    t.color("blue")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(radius_b)

# Начальная точка окружности B
start_point_b = (-x, -y)

t.color("green")
# Рисуем окружность B
t.penup()
t.goto(start_point_b)
t.pendown()
t.circle(radius_a)

print("-" * 50)
radius_b = 177

for u in range(1, num_circles):
    # Вычисляем положение следующей окружности
    x2 = start_point_b[0] + radius_b * math.sin(math.radians(angle * u))
    y2 = start_point_b[1] + radius_b * math.cos(math.radians(angle * u))
    print(f"x{u} = ({round(x2,1)}; {round(y2,1)})")
    #print(x, y)

    # Рисуем следующую окружность
    t.penup()
    t.goto(x2, y2)
    t.pendown()
    t.circle(radius_b)

# Скрываем черепаху и закрываем окно
t.hideturtle()
window.exitonclick()
