import pandas as pd

df1 = pd.read_csv('Sales1.csv')

df2 = pd.read_csv('Sales1.csv')

df3 = pd.read_csv('Sales3.csv')


frames = [df1, df2, df3]
print(frames)
result = pd.concat(frames)
print(result)
