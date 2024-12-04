



long_1 = int(input('Введите длину 1 параллелепипеда'))
width_1 = int(input('Введите ширину 1 параллелепипеда'))
high_1 = int(input('Введите высоту 1 параллелепипеда'))
long_2 = int(input('Введите  длину 2 параллелепипеда'))
width_2 = int(input('Введите ширину 2 параллелепипеда'))
high_2 = int(input('Введите высоту 2 параллелепипеда'))


V1 = long_1 * width_1 * high_1
V2 = long_2 * width_2 * high_2

if V1 == V2:
    print(' Обьемы равны')
else:
    if V1 > V2:
        print(' Первый обьем больше 2 обьема')
    else:
        print(' Второй обьем больше')


2
high = 7
w = high + 2
m = w //4
for i in range(1, high+1):
    if (i <= m):
        print(" " * (m-i) + "*" * (2*i) + " " * (w-2*i-2*m) + "*" *(2*i) + " " * (m-i))
    else:
      print(" " * (i - 2*m+1) + "*" * (w-2*(i-2*m+1)) + " " * (i - 2*m+1))



3
k = int(input('введите число'))
n = int(input('введите число'))

def comparion(k, n):
    if k < n:
        print('всё хорошо')
    elif k == n:
            print('всё хорошо')
    else:
        print('ошибка')

