
df_excel = pd.read_excel('список.xlsx')


def display_table():
    print(df_excel)
while True:
    display_table()
    try:
        row_index = int(input("Введите индекс строки : "))
        if row_index == -1:
            break
        col_index = int(input("Введите индекс колонки : "))
        if row_index < 0 or row_index >= df_excel.shape[0] or col_index < 0 or col_index >= df_excel.shape[1]:
            print("Ошибка: Индекс вне диапазона.")
            continue
        action = input("Введите 'внести' для ввода значения или 'очистить' для очистки ячейки: ").strip().lower()
        if action == 'внести':
            value = input("Введите значение для обновления: ")
            df_excel.iat[row_index, col_index] = value
            print("Значение внесено.")
        elif action == 'очистить':
            df_excel.iat[row_index, col_index] = None
            print("Значение очищено.")
        else:
            print("Ошибка: Неверное действие. Пожалуйста, введите 'внести' или 'очистить'.")
    except ValueError:
        print("Ошибка: Введите корректные значения.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
print("Программа завершена.")