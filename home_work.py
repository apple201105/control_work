import pandas as pd
from openpyxl import load_workbook
wb = load_workbook('список.xlsx')
ws = wb.active

ws['G1'] = "arithmetic mean"
ws['G2'] = '=СРЗНАЧ(B2:F2)'
ws['G3'] = '=СРЗНАЧ(B3:F3)'
ws['G4'] = '=СРЗНАЧ(B4:F4)'
ws['G5'] = '=СРЗНАЧ(B5:F5)'
ws['G6'] = '=СРЗНАЧ(B6:F6)'
ws['G7'] = '=СРЗНАЧ(B7:F7)'
ws['G8'] = '=СРЗНАЧ(B8:F8)'
ws['G9'] = '=СРЗНАЧ(B9:F9)'

wb.save('список.xlsx')
df_excel = pd.read_excel('список.xlsx')
print(df_excel)
