



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
