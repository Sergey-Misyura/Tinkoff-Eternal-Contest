'''Задача J. Торт

Соня с Сашей купили торт в форме выпуклого многоугольника на n вершинах.
Они хотят разделить этот торт на две равные части одним строго вертикальным разрезом.
А, именно, линия разреза на торте должна быть параллельна координатной оси O_y
Найдите x-координату, вдоль которой надо сделать искомый разрез.
Формат входных данных
В первой строке вводится число n — количество вершин многоугольника (1 ≤ n ≤ 1000)
В следующих n строках записаны записаны координаты вершин торта-многоугольника в порядке обхода.
Гарантируется, что координаты — целые числа, не превосходящие по модулю 10^3
Формат выходных данных
Выведите одно число — искомую x-координату. Ответ надо выводить с точностью не меньше 10^−6
Замечание
Первый тест — это квадрат, разделенный на две равные части.
Примеры данных
Пример 1
Ввод:
4
0 0
0 2
2 2
2 0
Вывод: 1.000000000'''

# Partial Solution 3 tests done

from statistics import mean

n = int(input()) # example: n = 4
coords = tuple(tuple(map(int,input().split())) for _ in range(n)) # example: coords = ((0,0), (2,0), (2,2), (0,2))


# calculate the area of a polygon
def area(coords):
    coords = list(coords)
    coords.append(coords[0]) 
    return 0.5*sum([coords[i][0]*coords[i+1][1] - coords[i+1][0]*coords[i][1] for i in range(len(coords)-1)]) #example: return 4


# calculate the intersection point of 2 lines
def intersection_point(line1, line2):
    '''
    line1 = ((2,0), (2,2)), line2 = ((1,0), (1,2))
    '''

    x1,y1,x2,y2 = *line1[0], *line1[1],
    x3,y3,x4,y4 = *line2[0], *line2[1],
    x = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) ) 
    y = ( (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )

    return (x,y)


# dividing a polygon into 2 polygons
def polygon_division(coords, x):
    
    poly1_coord = [] # example: poly1_coord = ((0,0), (0,2), (1,2), (1,0))
    poly2_coord = [] # example: poly2_coord = ((1,2), (2,2), (2,0), (1,0))
    coords_list = list(coords)
    coords_list.append(coords_list[0])
    
    for num in range(len(coords_list)-1):
        # first intersection point
        if (x >= coords_list[num][0]) and (x <= coords_list[num+1][0]):
            min_y, max_y = min(coords_list[num][1], coords_list[num+1][1])-1, max(coords_list[num][1], coords_list[num+1][1])+1
            first_point = intersection_point((coords_list[num], coords_list[num+1]), ((x, min_y), (x, max_y)))
            
            poly1_coord = coords_list[:num+1].copy()
            poly1_coord.append(first_point)
            start_poly2 = num+1 # num of first point from general polygon
        
        # second intersection point
        if (x <= coords_list[num][0]) and (x >= coords_list[num+1][0]):
            min_y, max_y = min(coords_list[num][1], coords_list[num+1][1])-1, max(coords_list[num][1], coords_list[num+1][1])+1
            second_point = intersection_point((coords_list[num], coords_list[num+1]), ((x, min_y), (x, max_y)))
            
            poly2_coord = coords_list[start_poly2:num+1].copy()
            poly2_coord.insert(0, first_point)
            poly2_coord.append(second_point)
            poly1_coord.append(second_point)
            poly1_coord += coords_list[num+1:-1]

    return poly1_coord, poly2_coord


# initial values for binary search
left_x = min(coords[:][1])
right_x = max(coords[:][1])
target_x = mean([left_x, right_x]) # start with mean(x)
area1 = 100
area2 = 0

# binary search
while area1 != area2:
    poly1_coord, poly2_coord = polygon_division(coords, target_x)
    area1 = area(poly1_coord)
    area2 = area(poly2_coord)
    if area1 > area2:
        right_x = target_x
        target_x = mean([left_x,target_x])
    elif area1 < area2:
        left_x = target_x
        target_x = mean([target_x,right_x])

print('%.9f' % target_x)