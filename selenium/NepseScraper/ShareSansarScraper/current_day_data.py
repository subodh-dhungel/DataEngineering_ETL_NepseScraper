from selenium.webdriver.common.by import By
import pandas as pd
import time
from ShareSansarScraper.selenium_driver import SeleniumDriver

class CurrentDayData:
    """Scraper for extracting table data from Sharesansar Market page."""
    
    def __init__(self, url="https://www.sharesansar.com/market", headless=True):
        self.url = url
        self.driver = SeleniumDriver(headless=headless).driver

    def current_market_indices(self):
        """Extract market table data from Sharesansar."""
        self.driver.get(self.url)
        time.sleep(5)

        try:
            table = self.driver.find_element(By.CLASS_NAME, "table")
            headers = [th.text.strip() for th in table.find_elements(By.TAG_NAME, "th")]

            data = []
            rows = table.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                cols = row.find_elements(By.TAG_NAME, "td")
                if cols:
                    data.append([col.text.strip() for col in cols])

            return headers, data

        except Exception as e:
            print(f"Error extracting table data: {e}")
            return [], []

    def close_driver(self):
        """Close the Selenium WebDriver."""
        self.driver.quit()