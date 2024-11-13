iphone Price Scraper for Daraz
This Python project scrapes iPhone price data from Daraz using BeautifulSoup for parsing HTML content and Selenium for handling dynamic web content. The scraper collects data on various iPhone models, including their names, prices, and links to their product pages.

Features
Dynamic Content Handling: Uses Selenium to load dynamic content that isn't available in the page source initially.
Efficient HTML Parsing: Extracts relevant data using BeautifulSoup for fast and efficient parsing.
CSV Export: Saves scraped data in a CSV file for easy analysis and reporting.
Requirements
Python 3.6+
Selenium: Automates the web browser for content loading.
BeautifulSoup: Parses the HTML content.
pandas: Handles CSV data export.
Install dependencies with:

bash
Copy code
pip install selenium beautifulsoup4 pandas
Additionally, you'll need to download the appropriate WebDriver (e.g., ChromeDriver or GeckoDriver) for Selenium and place it in your system PATH.

Usage
Set Up WebDriver: Download and set up the WebDriver based on your preferred browser (Chrome, Firefox, etc.).
Run the Script:
bash
Copy code
python scrape_daraz.py
View the Data: The output will be saved to iphone_prices.csv in the project directory.
