import pandas as pd

df1 = pd.read_csv('Sales1.csv')

df2 = pd.read_csv('Sales1.csv')


df = pd.concat([df1, df2])
print(df)