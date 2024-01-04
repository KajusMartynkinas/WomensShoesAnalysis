import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import re

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}


# response = requests.get(url, headers=headers)
# print(response)

service = Service('C:/Users/Aero/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')  # Replace with your ChromeDriver path
driver = webdriver.Chrome(service=service)

data = []

# Iterate through pages
for i in range(1, 61):
    url = f'https://www.aliexpress.com/w/wholesale-women-shoes.html?page={i}&g=n&SearchText=women+shoes'
    driver.get(url)

    # response = requests.get(url, headers=headers)
    #
    # soup = BeautifulSoup(response.content, 'html.parser')

    # Wait for the page to load
    time.sleep(2)  # Adjust time as necessary

    # Scroll down a fixed number of times
    for _ in range(17):  # Adjust the range for the number of scrolls
        driver.execute_script("window.scrollBy(0, 800);")  # Adjust the pixel value as needed
        time.sleep(1)  # Adjust based on site's loading behavior

    # Find elements by their class name or other attributes
    price_elements = driver.find_elements(By.CLASS_NAME, 'multi--price-sale--U-S0jtj')
    title_elements = driver.find_elements(By.CLASS_NAME, 'multi--titleText--nXeOvyr')
    sold_elements = driver.find_elements(By.CLASS_NAME, 'multi--trade--Ktbl2jB')

    for price, title, sold in zip(price_elements, title_elements, sold_elements):
        # Clean the title and price
        cleaned_title = title.text.strip()
        cleaned_price = re.sub(r'[^\d.]+', '', price.text)  # Removing non-alphanumeric characters
        cleaned_sold = sold.text.strip().replace(',', '').replace('+','').replace('K', '000').replace(' sold','')

        data.append({
            'title': cleaned_title,
            'price': cleaned_price,
            'sold': cleaned_sold
        })

    # for element in elements:
    #     data.append(element.text)

driver.quit()  # Close the browser

df = pd.DataFrame(data)
print(df)
df.to_csv('aliExpress.csv0', index = False)
# Printing or processing the data
# for title in data:
#     print(title)