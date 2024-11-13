from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

#open browser
browser = webdriver.Firefox()

#load webpage
browser.get("https://www.daraz.com.np")

browser.maximize_window()

#get input elements
search_input = browser.find_element(By.XPATH, '//*[@id="q"]')
search_button = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/form/div/div[2]/button')

#send input
search_input.send_keys("iphone")
search_button.click()

#take screenshot of webpage
browser.save_full_page_screenshot('\daraz\daraz.png')

#scrape products
products = []
print('Scraping page')
product = browser.find_elements(By.ID, "id-a-link")
price_list = browser.find_elements(By.CLASS_NAME, "currency--GVKjl")
for p in product:
    products.append(p.text)
for p in price_list:
    products.append(p.text)
browser.quit()

#extract data to csv file
df = pd.DataFrame(products)
print(df)
df.to_csv('products_daraz.csv', sep = '\t', index=False)