# coding=utf-8
"""
Задача 4. Наибольшее произведение-палиндром

Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""


def poly_detected():
    res = 0
    for i in range(100, 1000):
        for j in range(100, 100):
            temp_res = i * j
            if len(str(temp_res)) < 6:
                continue
            else:
                if str(temp_res)[0:3] == str(temp_res)[3:6][::-1] and temp_res > res:
                    res = temp_res
    return res


print(poly_detected())
