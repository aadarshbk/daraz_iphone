from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the Daraz Nepal URL you want to scrape
url = 'https://www.daraz.com.np/smartphones/'

# Use a context manager for the WebDriver to ensure it is properly closed
with webdriver.Chrome() as driver:
    while True:
        # Open the URL in the browser
        driver.get(url)

        # Wait for the page to load (adjust the time as needed)
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product-title')))

        # Extract product details, e.g., product names and prices
        product_names = [product.text for product in driver.find_elements(By.CSS_SELECTOR, '.product-title')]
        product_prices = [price.text for price in driver.find_elements(By.CSS_SELECTOR, '.price')]

        # Print the extracted data
        for name, price in zip(product_names, product_prices):
            print(f'Product Name: {name}, Price: {price}')

        # Ask the user if they want to continue scraping or quit
        user_input = input("Do you want to continue scraping (y/n)? ").lower()
        if user_input != 'y':
            break
