import pandas as pd

df1 = pd.read_csv('Sales1.csv', index_col=[0])

df2 = pd.read_csv('Sales1.csv', index_col=[0])

df3 = pd.read_csv('Sales1.csv', index_col=[0])


df = pd.concat([df1, df2,df3],axis=1, join='inner')
print(df)
