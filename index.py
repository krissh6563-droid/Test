import pandas as pd

df = pd.read_excel('RawData.xlsx')
df['09-28'] = pd.to_numeric(df['09-28'])

print(df.dtypes)
print(df['09-28'])

# Data Analysis Tasks
# Count the total number of rows
total_rows = len(df)

# Find the commodity with highest daily closing price and the corresponding price.
commodity = df['09-28'].max()
max_duration_row = df[df['09-28'] == df['09-28'].max()]

# Display the results
print("Total Number of rows are", total_rows)
print("Commodity with the highest daily closing price & Its corresponding price is",commodity)
print(max_duration_row)



