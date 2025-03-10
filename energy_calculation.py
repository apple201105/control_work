import pandas as pd

# Создаем начальную таблицу (DataFrame)
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Выводим начальную таблицу
print("Начальная таблица:")
print(df)

# Запрашиваем у пользователя индекс строки, индекс колонки и значение
try:
    row_index = int(input("Введите индекс строки (0, 1, 2): "))
    col_index = int(input("Введите индекс колонки (0 для 'A', 1 для 'B', 2 для 'C'): "))
    value = input("Введите значение для обновления: ")

    # Обновляем значение в таблице
    df.iat[row_index, col_index] = value

    # Выводим обновленную таблицу
    print("\nОбновленная таблица:")
    print(df)

except IndexError:
    print("Ошибка: Индекс вне диапазона.")
except ValueError:
    print("Ошибка: Введите корректные значения.")