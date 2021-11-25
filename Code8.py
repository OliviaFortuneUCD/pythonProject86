import pandas as pd

df1 = pd.read_csv('Sales1.csv')

df2 = pd.read_csv('Sales1.csv')

df3 = pd.read_csv('Sales3.csv')


df = pd.merge(df1, df2, left_on='Key', right_on=('Key'), how=('left'))
print(df)

dfx= pd.merge(pd.merge(df1,df2,on='Key'),df3,on='Key')
print(dfx)