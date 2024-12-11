import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)
# Сохранение в CSV
df.to_csv('output.csv', index=False)

# Сохранение в Excel
df.to_excel('output.xlsx', index=False)