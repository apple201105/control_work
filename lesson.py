import pandas as pd
df_excel = pd.read_excel('Лист.xlsx')
if df_excel.select_dtypes(include='number').empty:
    print("В таблице нет числовых данных.")
else:
    df_excel['Среднее арифметическое'] = df_excel.mean(axis=1)
    df_excel['Дисперсия'] = df.var(axis=1)
    output_file_path = "output.xlsx"
    df_excel.to_excel(output_file_path, index=False)

    print(f"Результаты сохранены в файл: {output_file_path}")



# Код для нахождения дисперсии по строкам DataFrame

import pandas as pd


def calculate_variance_by_row(df):
    numeric_columns = df.select_dtypes(include=['number'])
    df['dISP'] = numeric_columns.var(axis=1)
    return df

df = pd.read_excel('список.xlsx')
df = calculate_variance_by_row(df)
print(df)
