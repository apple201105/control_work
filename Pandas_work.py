import pandas as pd
from openpyxl import load_workbook
wb = load_workbook('список.xlsx')
ws = wb.active
df_excel = pd.read_excel('список.xlsx')
row_index = int(input('Введите индекс строки:'))
column_index = int(input('Введите индекс колонки:'))
meaning = int or str(input('Введите значение,которое Вы хотите ввести в таблицу:'))
df_excel.iat[row_index, column_index] = meaning
print(df_excel)
