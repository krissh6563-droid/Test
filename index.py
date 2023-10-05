import pandas as pd

df = pd.read_excel('RawData.xlsx')

print(df.dtypes)
print(df['09-27'].max())
#print(df['09-27'].max())



