# coding=utf-8
from TimeIt import timeit
'''
Задача 3. Наибольший простой делитель

Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?
'''
@timeit
def get_greatest_divisor():
    max_simple_digit = 0
    result = 0
    super_num = 600851475143
    test = 10000

    for num in range(test):
        if num%2 == 0 or num % 5 == 0 or num % 3 == 0:
            continue
        else:
            result = num
            for digit in range(1, num):
                if digit != num and digit != 1 and num % digit == 0:
                    result = 0
                else:
                    if max_simple_digit < result:
                        max_simple_digit = result

    print(max_simple_digit)


get_greatest_divisor()
#5244.12 ms (отвратительно)

