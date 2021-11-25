import pandas as pd

data1 = {
  "name": ["Sally", "Mary", "John"],
  "age": [21, 41, 31]
}

data2 = {
  "qualified": [True, False, False]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

newdf = df1.join(df2)

print(newdf)