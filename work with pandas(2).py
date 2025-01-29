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
        act = input("Введите 'внести' для ввода значения или 'очистить' для очистки ячейки или подсчитать среднее значение или 'мин и макс': ").strip().lower()
        if act == 'внести':
            val = input("Введите значение для обновления: ")
            df_excel.iat[row_ind, col_ind] = val
            print("Значение внесено.")
        elif act == 'очистить':
            df_excel.iat[row_ind, col_ind] = None
            print("Значение очищено.")
        elif act == 'среднее значение':
            choise = str(input('Введите "колонка" или "столбец":'))
            if choise == "колонка":
                col_name = str(input('Введите название калонки'))
                print(df_excel.iloc[col_ind].mean())
            elif choise == "столбец":
                row_name = str(input('Введите название строки'))
                print(df_excel.iloc[row_ind].mean())
        elif act == 'мин и макс':
            column_name = str(input('введите название колонки'))
            row_index = int(input('введите индекс строки'))

            if column_name in df_excel.columns:
                min_value = df_excel[column_name].min()
                max_value = df_excel[column_name].max()
                print(f'Минимальное значение в колонке "{column_name}": {min_value}')
                print(f'Максимальное значение в колонке "{column_name}": {max_value}')
            else:
                print(f'Колонка "{column_name}" не найдена в таблице.')

            if row_index < len(df_excel):
                min_value_row = df_excel.iloc[row_index].min()
                max_value_row = df_excel.iloc[row_index].max()
                print(f'Минимальное значение в строке {row_index}: {min_value_row}')
                print(f'Максимальное значение в строке {row_index}: {max_value_row}')
            else:
                print(f'Строка с индексом {row_index} не найдена в таблице.')
    
    except ValueError:
        print("Ошибка: Введите корректные значения.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    print("Программа завершена.")
