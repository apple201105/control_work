def time(S,u):
    if u == 0 :
        print('Деление на ноль')
    else:
         return S/u


S = int(input('Введите расстояние:'))
u = int(input('Введите скорость:'))
print(time(S,u))