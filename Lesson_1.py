import math

def circum_of_the_circle(r):
    return math.pi * 2 * r
def area_of_the_circle(r):
    return math.pi * r ** 2

r = int(input('Введите радиус:'))
print(circum_of_the_circle(r))
print(area_of_the_circle(r))