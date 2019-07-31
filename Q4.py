# coding=utf-8
import timeit
"""
Задача 4. Наибольшее произведение-палиндром

Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""
def is_poly(num):
    start = str(num)
    end = len(start) - 1
    for i in range(0, end):
        if start[i] != start[end - i]:
            return False

    return True

def poly_detected():
    max = 0
    for i in range(1000, 100, -1):
        for j in range(1000, 100, -1):
            tmp = i * j
            if tmp > max and is_poly(tmp):
                max = tmp
    return max


print(poly_detected())
# 205.15 ms


