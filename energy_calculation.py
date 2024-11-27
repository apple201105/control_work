

def energy_calc(m,u):
    return 0.5 * m * u ** 2


m = int(input('введите массу:'))
u  = int(input('введите скорость:'))
print(energy_calc(m,u))
