

import pandas as pd

Data_Frame = str(input('Введите название таблицы:'))
def calc_var(df):
    numeric_columns = df.select_dtypes(include=['number'])
    df['Disp'] = numeric_columns.var(axis=1)
    return df


df = pd.read_excel(Data_Frame)
df = calc_var(df)
print(df)
