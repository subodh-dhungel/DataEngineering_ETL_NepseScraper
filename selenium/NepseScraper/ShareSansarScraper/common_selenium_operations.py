from ShareSansarScraper.selenium_driver import SeleniumDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class Operations:
    """Parent class to handle common Selenium Operations"""
    def __init__(self,url,headless=True):
        self.url = url
        self.headless = headless

    def extract_table_data(self, xpath):
        """Extract table data using an XPath."""
        with SeleniumDriver(headless=self.headless) as driver:
            driver.get(self.url)

            try:
                # Wait for the table element to be present
                table = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )

                # Wait for the headers to be present (optional, if headers take time to load)
                headers = [th.text.strip() for th in table.find_elements(By.TAG_NAME, "th")]

                # Wait for rows to be present and extract data
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
            
    def locateElement(self, identifier:str, identifier_type, wait_time:int = 60):
        try:
            table = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((identifier_type, identifier))
            )
        except TimeoutError as err:
            print(err)

