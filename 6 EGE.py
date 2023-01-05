count = 0
for x in range(1, 10):
    for y in range(1, 10):
        if -x / 3 ** 0.5 + 10 > y > x / 3 ** 0.5:
            count += 1
print(count) #47210

import turtle as t  # Подключим модуль черепашка
k = 30
t.left(90)
t.speed(10)
for i in range(10):  # пропишем алгоритм построения фигуры по условию
    t.forward(5 * k)
    t.right(60)
t.up()
t.speed(10)  # Увеличим скорость черепашки
for x in range(10, -5, - 1):  # Алгоритм построения точек
    for y in range(10, -10, - 1):
        t.goto(x * k, y * k)
        t.dot(3)  # точки размером 4 пикселя
t.done() #47394

count = 0
for x in range(1, 12):
    for y in range(1, 12):
        if (y > x * 3 ** 0.5) or (y < (x - 8) * 3 ** 0.5) or (y > (64 - 16)**(1/2)):
            count += 1
print(count) #47403