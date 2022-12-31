'''Задача E. Тестирование

Во время разработки некоторой задачи Саша решил сгенерировать несколько новых тестов.
Каждый тест Саши должен представлять собой натуральное число, не меньшее l и не большее r.
Кроме того, натуральное число в тесте обязательно должно состоять из одинаковых цифр.
Например, число 999 подходит под это требование, а число 123 — нет.
Какое максимальное число различных тестов сможет создать Саша?
Формат входных данных
В единственной строке вводятся два натуральных числа l, r (1 ≤ l, r ≤ 10^18) — ограничения на тесты Саши.
Обратите внимания, что эти числа не вместятся в 32-битный тип данных, используйте 64-битный при необходимости
Формат выходных данных
Выведите одно число — количество тестов, которое может сделать Саша.
Замечание
В первом тесте Саше подходят номера [4,5,6,7].
Во втором тесте подходят все числа, кратные 11, от 11 до 99.
Примеры данных
Пример 1
Ввод: 4 7
Вывод: 4
Пример 2
Ввод: 10 100
Вывод: 9'''

# OK 69 tests done

l, r = map(int, input().split())

nums = [1,2,3,4,5,6,7,8,9]
second = nums.copy()
n = 0

for _ in range(len(str(r))-1):
    for i in range (0,9):
        second[i] = second[i]*10 + i+1
        nums.append(second[i])

for num in nums:
    n +=1 if num in range(l, r+1) else 0

print(n)