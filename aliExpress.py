import pandas as pd
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

service = Service('C:/Users/Aero/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

data = []

for i in range(1, 61):
    url = f'https://www.aliexpress.com/w/wholesale-women-shoes.html?page={i}&g=n&SearchText=women+shoes'
    driver.get(url)

    time.sleep(2)

    for _ in range(17):
        driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(1)

    price_elements = driver.find_elements(By.CLASS_NAME, 'multi--price-sale--U-S0jtj')
    title_elements = driver.find_elements(By.CLASS_NAME, 'multi--titleText--nXeOvyr')
    sold_elements = driver.find_elements(By.CLASS_NAME, 'multi--trade--Ktbl2jB')

    for price, title, sold in zip(price_elements, title_elements, sold_elements):
        cleaned_title = title.text.strip()
        cleaned_price = re.sub(r'[^\d.]+', '', price.text)
        cleaned_sold = sold.text.strip().replace(',', '').replace('+','').replace('K', '000').replace(' sold','')

        data.append({
            'title': cleaned_title,
            'price': cleaned_price,
            'sold': cleaned_sold
        })

driver.quit()

df = pd.DataFrame(data)
print(df)
df.to_csv('aliExpress.csv0', index = False)