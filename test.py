from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Initialize Chrome browser
driver = webdriver.Chrome(options=Options())

#Maximize the browser window
driver.maximize_window() 

# Step 2: Navigate to the provided URL
driver.get("http://www.sunsirs.com/futures-price-2023-0927-daily.html")

#Find the table by xpath
table = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[1]/div/div[4]/table/tbody')


    
# scrap table row data
table_data = []
for tr in table.find_elements(By.XPATH,'//tr'):
    row = [item.text for item in tr.find_elements(By.XPATH, './/td')]
    table_data.append(row)

driver.close()

# Pandas to Store into a DataFrame
df = pd.DataFrame(table_data, columns=['Commodity','Sector','09-27','09-28','Change'])
df.drop(0,inplace=True)

df['09-27'] = pd.to_numeric(df['09-27'].str.replace(',',''))
df['09-28'] = pd.to_numeric(df['09-28'].str.replace(',',''))

# Save the extracted data with the sheet name as "Raw Data" in an Excel workbook
file_name = 'RawData.xlsx'
df.to_excel(file_name)


# Data Analysis Tasks
# Count the total number of rows
total_rows = len(df)

# Find the commodity with highest daily closing price and the corresponding price.
commodity = df['09-28'].max()
max_duration_row = df[df['09-28'] == df['09-28'].max()]
# Display the results
print("Total Number of rows are", total_rows)
print(max_duration_row)
print("Commodity with the highest daily closing price & Its corresponding price is",commodity)



