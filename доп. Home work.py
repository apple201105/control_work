import pandas as pd
from openpyxl import load_workbook
wb = load_workbook('список.xlsx')
ws = wb.active
ws['G1'] = "AM"
ws['G2'] = (ws['B2'].value+ws['C2'].value+ws['D2'].value+ws['E2'].value+ws['F2'].value)/5
ws['G3'] = (ws['B3'].value+ws['C3'].value+ws['D3'].value+ws['E3'].value+ws['F3'].value)/5
ws['G4'] = (ws['B4'].value+ws['C4'].value+ws['D4'].value+ws['E4'].value+ws['F4'].value)/5
ws['G5'] = (ws['B5'].value+ws['C5'].value+ws['D5'].value+ws['E5'].value+ws['F5'].value)/5
ws['G6'] = (ws['B6'].value+ws['C6'].value+ws['D6'].value+ws['E6'].value+ws['F6'].value)/5
ws['G7'] = (ws['B7'].value+ws['C7'].value+ws['D7'].value+ws['E7'].value+ws['F7'].value)/5
ws['G8'] = (ws['B8'].value+ws['C8'].value+ws['D8'].value+ws['E8'].value+ws['F8'].value)/5
ws['G9'] = (ws['B9'].value+ws['C9'].value+ws['D9'].value+ws['E9'].value+ws['F9'].value)/5
ws['H1'] = "Average"
ws['H2'] = '= AVERAGE(B2:F2)'
ws['H3'] = '= AVERAGE(B3:F3)'
ws['H4'] = '= AVERAGE(B4:F4)'
ws['H5'] = '= AVERAGE(B5:F5)'
ws['H6'] = '= AVERAGE(B6:F6)'
ws['H7'] = '= AVERAGE(B7:F7)'
ws['H8'] = '= AVERAGE(B8:F8)'
ws['H9'] = '= AVERAGE(B9:F9)'
wb.save('список.xlsx')
df_excel = pd.read_excel('список.xlsx')
print(df_excel)

