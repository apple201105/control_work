import pandas as pd
df_excel = pd.read_excel('список.xlsx')
ind_colum = input("Введите индексы столбцов: P.S пожалуйста раздилите все индексы запятыми, а то работать не будет ")
indices = [int(i) for i in ind_colum.split(',')]
valid_indices = [i for i in indices if 0 <= i < len(df_excel.columns)]
sel_col = df_excel.iloc[:, valid_indices]
print(sel_col)
