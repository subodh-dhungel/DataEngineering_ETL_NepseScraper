from ShareSansarScraper import constants
from ShareSansarScraper.constants import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ShareSansarScraper.selenium_driver import SeleniumDriver

class DatewiseData:
    def __init__(self, date):
        self.date = date
        self.url = constants.ss_datewise_market_url

    def _perform_search(self, driver):
        """Helper function to perform the search operation"""
        # Wait for search box and input date
        searchbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_datewise_market_input_box))
        )
        searchbox.clear()
        searchbox.send_keys(self.date)

        # Wait for search button and click
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_datewise_market_search_button))
        )
        search_button.click()

    def datewise_market_indices(self):
        """Extracts datewise market indices value"""
        with SeleniumDriver() as selenium_driver:
            driver = selenium_driver.get_driver()
            driver.get(self.url)

            self._perform_search(driver)

            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, constants.xpath_datewise_market_summary_table))
            )

            headers, data = selenium_driver.extract_table_data(constants.xpath_datewise_market_summary_table, self.url)
            return headers, data

    def datewise_sectorwise_summary(self):
        """Extracts sector-wise summary table"""
        with SeleniumDriver() as selenium_driver:
            driver = selenium_driver.get_driver()
            driver.get(self.url)

            self._perform_search(driver)

            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, xpath_datewise_sector_summary_table))
            )

            headers, data = selenium_driver.extract_table_data(xpath_datewise_sector_summary_table, self.url)
            return headers, data
