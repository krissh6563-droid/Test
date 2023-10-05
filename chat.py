# Import necessary libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# Set the URL of the web page to scrape
url = "URL_TO_THE_WEB_PAGE"

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(executable_path="PATH_TO_CHROME_DRIVER")

# Navigate to the provided URL
driver.get(url)

# Find the table with the title "Futures Daily Price"
table = driver.find_element(By.XPATH, "//table[@summary='Futures Daily Price']")

# Scrape data from the table
table_data = []
for row in table.find_elements(By.TAG_NAME, 'tr'):
    row_data = [cell.text for cell in row.find_elements(By.TAG_NAME, 'td')]
    table_data.append(row_data)

# Close the web browser
driver.quit()

# Convert scraped data into a Pandas DataFrame
df = pd.DataFrame(table_data[1:], columns=table_data[0])

# Data Analysis Tasks

# a. Count the total number of rows
total_rows = len(df)

# b. Find the commodity with the highest daily closing price and the corresponding price
df['Closing Price'] = df['Closing Price'].str.replace(',', '').astype(float)
max_price_row = df[df['Closing Price'] == df['Closing Price'].max()]
commodity_with_highest_price = max_price_row['Commodity'].values[0]
highest_price = max_price_row['Closing Price'].values[0]

# Create an Excel writer
excel_writer = pd.ExcelWriter('scraped_data.xlsx', engine='xlsxwriter')

# Save the data to an Excel workbook with the sheet name "Raw Data"
df.to_excel(excel_writer, sheet_name='Raw Data', index=False)

# Close the Excel writer
excel_writer.save()

# Print the results of data analysis tasks
print(f'Total number of rows in the table: {total_rows}')
print(f'Commodity with the highest daily closing price: {commodity_with_highest_price}')
print(f'Highest daily closing price: {highest_price}')

# Close the web browser
driver.quit()

import pandas as pd

# Convert a specific column to numeric
df['Column_Name'] = pd.to_numeric(df['Column_Name'], errors='coerce')

# The 'errors' parameter handles how errors during conversion are handled.
# 'coerce' will convert non-convertible values to NaN (Not a Number).
