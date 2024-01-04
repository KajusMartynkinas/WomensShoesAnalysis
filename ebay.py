import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import re

# Set up the WebDriver
service = Service('C:/Users/Aero/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')  # Replace with your ChromeDriver path
driver = webdriver.Chrome(service=service)

data = []

for page_num in range(1, 82):  # Looping through 80 pages
    url = f'https://www.ebay.com/sch/3034/i.html?_from=R40&_nkw=womens+shoes&_ipg=60&_dmd=1&rt=nc&_pgn={page_num}'
    driver.get(url)

    # Scroll down the page gradually
    total_scrolls = 11
    scroll_pause_time = 1  # Pause time between scrolls, in seconds
    for i in range(total_scrolls):
        driver.execute_script("window.scrollBy(0, 1500);")
        time.sleep(scroll_pause_time)

    # Use Selenium to get the page source after scrolling
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    scrape_title = soup.find_all('div', class_='s-item__title')
    scrape_price = soup.find_all('div', class_='s-item__details clearfix')
    scrape_sold = soup.find_all('span', class_='s-item__dynamic s-item__quantitySold')

    price_pattern = r'\$\d{1,3}(,\d{3})*(\.\d{2})?'

    for title, price in zip(scrape_title, scrape_price):
        title_text = title.get_text().strip()
        if title_text == "Shop on eBay":
            title_text = 'Title Error'

        price_text_full = price.get_text()
        price_match = re.search(price_pattern, price_text_full)
        if price_match:
            price_text = float(price_match.group().replace('$', '').replace(',',''))
        else:
            price_text = 'Price not found'

        # Handle the 'sold' information
        sold_index = scrape_title.index(title)  # Get the index of the current title
        if sold_index < len(scrape_sold):
            sold_text = int(scrape_sold[sold_index].get_text().strip().replace('+ sold', '').replace(',', '').replace(
                ' sold', ''))
        else:
            sold_text = '0'  # Default value if 'sold' data is not available

        data.append({
            'title': title_text,
            'price': price_text,
            'sold': sold_text
        })

# Convert to DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('ebay.csv', index=False)

# Close the WebDriver
driver.quit()