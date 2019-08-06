# coding=utf-8
from TimeIt import timeit
'''
Задача 2. Четные числа Фибоначчи

Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
'''
@timeit
def sumFib():
    first = 0
    second = 1
    sum = 0
    while sum < 4000000:
        tmp = first + second
        first = second
        second = tmp
        if second % 2 == 0:
            sum += second
    return sum


print(sumFib())
#0.03 ms

