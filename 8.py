'''Задача H. Переговорка

Миша сидел в переговорке и решил нарисовать ее план на листке бумаги.
Когда он закончил рисовать план переговорки, он положил лист с планом на пол переговорки.
Теперь ему стало интересно: а есть ли на плане точка, которая лежит ровно на том месте пола, за которое она отвечает?
Помогите ему найти эту точку.
Формат входных данных
Переговорка и ее план имеют форму прямоугольника.
Первая строка входного файла содержит два вещественных числа:
координаты X и Y переговорки (1 ≤ X ≤ 1000, 1 ≤ Y ≤ 1000).
Координаты углов переговорки равны (0, 0), (X, 0), (X, Y), (0, Y).
Во второй строке файла даются восемь вещественных чисел, описывающих положение углов плана переговорки.
Сначала вводятся координаты того угла плана,
который соответствует углу переговорки с координатами (0, 0), затем — (X, 0),(X, Y), наконец, (0, Y).
Гарантируется, что входные данные корректны, то есть план является прямоугольником,
линейные размеры которого соответствуют размерам переговорки, а также он не выходит за границы перегородки.
Все числа во входном файле вещественные, заданы с точностью 5 знаков после десятичной точки.
План выполнен в масштабе не менее 0,0001 и строго менее 1.
Формат выходных данных
Выведите два вещественных числа — координаты неподвижной точки в координатах переговорки.
Выводить число нужно с точностью не менее четырех знаков после запятой.
Замечание
Заметьте, что для читаемости условий входные данные в примере даются с меньшим количеством десятичных знаков.
В реальных тестовых данных в координатах будут дополнительные нули на конце.
Примеры данных
Пример 1
Ввод:
10 5
3.0 2.5 1.0 2.5 1.0 1.5 3.0 1.5
Вывод: 2.5000 2.0833'''

# 0 tests done
import math

X, Y = map(int, input().split())
coord = list(map(float, input().split()))

len_x = math.sqrt((coord[2]-coord[0])**2 + (coord[3]-coord[1])**2)
k = X/len_x
fi = math.atan2(0, X) - math.atan2(coord[3] - coord[1], coord[2] - coord[0])

y = (Y*(1-math.cos(fi))-k*X*math.cos(fi))/((1-k*math.sin(fi))*(1-math.cos(fi))+k**2*math.sin(fi)*math.cos(fi))

x = (X+k*y*math.sin(fi))/(1 - math.cos(fi))

print(round(x, 4), round(y,4))