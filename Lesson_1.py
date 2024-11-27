import math


def determining_the_time(h):
    res = 2 * h / 9.8
    return math.sqrt(res)

h = int(input('Введите высоту:'))
print(determining_the_time(h))
