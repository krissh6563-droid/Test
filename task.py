from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from bs4 import BeautifulSoup

# Initialize Chrome browser
driver = webdriver.Chrome(options=Options())

#Maximize the browser window
driver.maximize_window() 

# Step 2: Navigate to the provided URL
driver.get("http://www.sunsirs.com/futures-price-2023-0927-daily.html")

#Find the table by xpath
table = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[1]/div/div[4]/table/tbody')

soup = BeautifulSoup(table.get_attribute('outerHTML'), "html.parser")

table_data = []
for row in soup.find_all('tr'):
    columns = row.find_all('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    table_data.append(output_row)

driver.quit()

df = pd.DataFrame(table_data, columns=['Commodity','Sector','09-27','09-28','Change'])
df.drop(0,inplace=True)

#df['Column1'] = pd.to_numeric(df['Column1'].str.replace(',', ''), errors='coerce')

df['09-28'] = pd.to_numeric(df['09-28'].str.replace(',',''))
# Save the extracted data with the sheet name as "Raw Data" in an Excel workbook
print(df['09-28'].max())
file_name = 'NewRawData.xlsx'
df.to_excel(file_name)




#df = pd.read_excel('NewRawData.xlsx')


