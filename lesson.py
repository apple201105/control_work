import pandas as pd


# Чтение Excel-файла
df_excel = pd.read_excel('список.xlsx')

# Посмотреть первые 5 строк
print(df_excel.head())

# Посмотреть информацию о таблице
print(df_excel.info())
