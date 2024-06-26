from flask import Flask, render_template_string, request
from datetime import datetime
import pytz

error_files=[]
try:
    from bs4 import BeautifulSoup
    import requests
    import re
    import pandas as pd
    from io import BytesIO

    def get_html_document(url):
        response2 = requests.get(url)
        return response2.text

    url_to_scrape = "https://www.nj.gov/labor/ea/osec/wall.shtml"
    html_document = get_html_document(url_to_scrape)

    soup = BeautifulSoup(html_document, 'html.parser')

    # Extract links with href attributes containing URLs ending in ".xlsx"
    for link in soup.find_all('a', attrs={'href': re.compile(r"\.xlsx$")}):
        site="https://www.nj.gov"+link.get('href')
    # Download the Excel file from the URL
    response2 = requests.get(site)
    content = response2.content

    # Read the Excel file content into a DataFrame
    df2 = pd.read_excel(BytesIO(content))
    df2.columns = df2.iloc[1]  # Set the first row as column names
    df2 = df2.iloc[2:]  # Remove the first row which is now the column names

    df2.rename(columns={
        "Name of Employer/DBA": "Name",
        "Principal Address of Employer": "Details",
        "Violation(s)": "Exclusion Type"
    }, inplace=True)
    #df2['Source'] = 'https://www.nj.gov/labor/ea/osec/wall.shtml'
    df2['Source']='The Wall'
    df2=df2[['Name','Details','Source']]
except Exception as e:
    print(e)
    error_files.append("The Wall")
#########################################################################################################
try:
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
    #chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    #chrome_options.add_argument("--disable-dev-shm-usage")

    # Set up the Selenium WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    # Load the webpage
    driver.get(url)
    all_rows_data = []

    # Wait for the element to be located
    try:
        scrollbar = WebDriverWait(driver, 40).until(
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
    df['Source']='NJ Wage Debarment List'
    df.reset_index(drop=True, inplace=True)
    df.rename(columns={0: "Name",}, inplace=True)
except Exception as e:
    print(e)
    error_files.append("NJ Wage Debarment List")
##################################################################################
try:
    url = "https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/SDN.CSV"

    df3 = pd.read_csv(url)
    df3.iloc[:,2]=df3.iloc[:,2].astype(str).replace('-0- ','Entity')
    df3['details']=df3.iloc[:,2]+"-"+df3.iloc[:,11]
    df3=df3.iloc[:,[1,12]]
    df3.columns=['Name','Details']
    df3['Details']=df3['Details'].str.replace('-0-','')
    df3['Source']='OFAC Sanctions List'
    df3=df3[['Name','Details','Source']]
except Exception as e:
    print(e)
    error_files.append("OFAC Sanctions List")
#######################################################################################
try:
    import PyPDF2
    import requests
    import io
    import re

    url = 'https://www.nj.gov/treasury/purchase/pdf/Chapter25List.pdf'

    response = requests.get(url)
    f = io.BytesIO(response.content)
    reader = PyPDF2.PdfReader(f)
    pages = reader.pages
    # get all pages data
    text = "".join([page.extract_text() for page in pages])

    # Open the text file for reading
    filtered_lines = re.findall(r'\b\d+\.\s.*', text)


    pattern = r'^(\d+)\.\s(.+)$'

    # Initialize lists to store extracted data
    numbers = []
    names = []

    # Extract data using regex
    for line in filtered_lines:
        match = re.match(pattern, line)
        if match:
            numbers.append(match.group(1))
            names.append(match.group(2))

    # Create DataFrame
    df4 = pd.DataFrame({'Name': names})
    #df4['Exclusion Type'] = ''
    df4['Source'] = 'nj.gov Treasury (Iran)'

    df4['Details']='N/A'
    df4=df4[['Name','Details','Source']]
except Exception as e:
    print(e)
    error_files.append("nj.gov Treasury (Iran)")
##########################################################################################
try:
    merged_df = pd.concat([df, df2, df3, df4], ignore_index=True)
    #merged_df.head()
    merged_df.to_excel("/home/gpanj1/mysite/data.xlsx",index=False)
except Exception as e:
    print(e)
    error_files.append("Merge")
if error_files:
    print(error_files)
else:
    error_files.append("None")
    from datetime import datetime
    import pytz
    merged_df.to_excel("data.xlsx",index=False)
    with open("/home/gpanj1/mysite/last_updated.txt", 'w') as file:
        utc_now = datetime.now(pytz.utc)
        eastern = pytz.timezone('US/Eastern')
        last_updated = utc_now.astimezone(eastern).strftime("%m-%d-%Y %H:%M:%S")
        file.write(last_updated)
#merged_df.to_excel("data.xlsx",index=False)
with open("/home/gpanj1/mysite/error.txt", 'w') as file:
    # Join the list items into a single string separated by spaces
    single_line = ", ".join(error_files)
    # Write the single line string to the file
    file.write(single_line)
