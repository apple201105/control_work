import pandas as pd
df_excel = pd.read_excel('список.xlsx')


def work_pandas():
    print(df_excel)
while True:
    work_pandas()
    try:
        row_ind = int(input("Введите индекс строки : "))
        if row_ind == -1:
            break
        col_ind = int(input("Введите индекс колонки : "))
        if row_ind < 0 or row_ind>= df_excel.shape[0] or col_ind < 0 or col_ind >= df_excel.shape[1]:
            print(" Индекс вне диапазона.")
            continue
        act = input("Введите 'внести' для ввода значения или 'очистить' для очистки ячейки: ").strip().lower()
        if act == 'внести':
            val = input("Введите значение для обновления: ")
            df_excel.iat[row_ind, col_ind] = val
            print("Значение внесено.")
        elif act == 'очистить':
            df_excel.iat[row_ind, col_ind] = None
            print("Значение очищено.")
        else:
            print(" Пожалуйста, введите 'внести' или 'очистить'.")
    except ValueError:
        print("Ошибка: Введите корректные значения.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
print("Программа завершена.")
