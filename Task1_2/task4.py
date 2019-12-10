# Написать функцию get_min_function(), которая:
# 1) принимает числовую последовательность sequence
# (любой итерируемый объект, возращащий int или float)
# и одну или несколько функций;
# 2) возвращает одну из переданных функций,
# сумма значений которой на всех элементах в sequenbce наименьшая,
# если таких функций несколько,
# последнюю (по порядку последовательности функций) из них.

from math import *


def get_min_function(numbers, *functions):

    result = []

    for func in functions:
        func_result = 0

        for numb in numbers:
            func_result += func(numb)

        result.append(func_result)

    return functions[result.index(min(result))]


def get_min_function_upgrade(numbers, *functions):
    return functions[min((val, idx) for (idx, val) in enumerate([sum([func(numb) for numb in numbers]) for func in functions]))[1]]


print(get_min_function_upgrade(range(-2, 10), sin, cos, exp))
