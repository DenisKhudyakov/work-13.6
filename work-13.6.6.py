import math

import numpy
import numpy as np
#  D = x^3 − 3x^2 − 12x + 10, где x — глубина кладки в метрах, а D — уровень опасности в условных единицах.

def formula(x):
  return x ** 3 - 3 * x ** 2 - 12 * x + 10

#Первый способ
def safe_lvl(danger_lvl):
    for i in np.arange(0, 4, 0.001):
        result = "{:.2f}".format(round(formula(i), 2))
        if math.isclose(float(result), danger_lvl):
            print('Приблизительная глубина безопасной кладки: ', i, 'm')

# Второй способ
def calculate_safe_depth(danger_lvl):
    min_depth = 0
    max_depth = 4
    result = (min_depth + max_depth) / 2

    while abs(formula(result)) >= danger_lvl:
        if abs(formula(min_depth)) < abs(formula(max_depth)):
            max_depth = result
        else:
            min_depth = result

        result = (min_depth + max_depth) / 2
    return result


def main_function():
    accept_danger_lvl = float(input('Введите максимально допустимый уровень опасности: '))
    result = calculate_safe_depth(accept_danger_lvl)
    print('Приблизительная глубина безопасной кладки: ', result, 'm')


safe_lvl(0.1)