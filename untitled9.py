from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
url = "https://app.powerbigov.us/view?r=eyJrIjoiZDQxYTM0MDMtMGQ2Mi00ZTRkLThmNzQtNTYyYjBhNjhiMTQyIiwidCI6IjUwNzZjM2QxLTM4MDItNGI5Zi1iMzZhLWUwYTQxYmQ2NDJhNyJ9"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the Selenium WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Load the webpage
driver.get(url)
all_rows_data = []

# Wait for the element to be located
try:
    scrollbar = WebDriverWait(driver, 0).until(
        EC.presence_of_element_located((By.CLASS_NAME, "mid-viewport"))
    )
except:
    print("Element not found. Check if the class name is correct or the element exists.")
    driver.quit()
    exit()

# Get the height of the table
table_height = driver.execute_script("return arguments[0].scrollHeight", scrollbar)
c=1
# Perform scrolling until the end of the table
while True:
    time.sleep(1.5)
    rows = driver.find_elements(By.CLASS_NAME, "row")
    for row in rows:
        cells = row.find_elements(By.CLASS_NAME, "pivotTableCellWrap")
        row_data = [cell.text for cell in cells]
        print(row_data)
        if row_data not in all_rows_data:  # Avoid adding duplicate rows
            all_rows_data.append(row_data)
    # Scroll down
    driver.execute_script("arguments[0].scrollTop +=arguments[1]", scrollbar,150)
    
    # Wait for a brief moment for the content to load
    
    c+=1
    # Break the loop if the scrollbar height hasn't changed (reached the bottom)
    
    #if new_table_height == table_height:
    #    break
    if c==20:
        break
    

# Extract row data
    
        #print(row_data)
    #new_table_height = driver.execute_script("return arguments[0].scrollHeight", scrollbar)
    #table_height = new_table_height
    # Close the browser window
driver.quit()
import pandas as pd
df = pd.DataFrame(all_rows_data)


df[2] = pd.to_datetime(df[2], errors='coerce')
df = df.dropna(subset=[2])
df['Details'] = df[3] + ' ' + df[5] + ' ' + df[6] + ' ' + df[7]

# Select only relevant columns
df = df[[0, 'Details']]
df['source']='NJ Prevailing Wage Debarment List'
df.reset_index(drop=True, inplace=True)
df.rename(columns={0: "Name",}, inplace=True)
df.to_excel("powerbi_data2.xlsx")
