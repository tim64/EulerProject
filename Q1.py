# coding=utf-8
from TimeIt import timeit
'''
Задача 1. Числа, кратные 3 или 5

Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел - 23.

Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
'''
@timeit
def sum1000():
    sum = 0
    for number in range(1000):
        if number % 3 == 0 or number % 5 == 0:
            sum += number
    return sum


print(sum1000())
#0.43 ms
