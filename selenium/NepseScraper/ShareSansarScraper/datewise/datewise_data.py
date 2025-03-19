from ShareSansarScraper import constants
from ShareSansarScraper.constants import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ShareSansarScraper.selenium_driver import SeleniumDriver

class DatewiseData:
    def __init__(self, date):
        self.date = date
        self.driver = SeleniumDriver(headless=False).get_driver()
        self.url = constants.ss_datewise_market_url

    def _perform_search(self):
        """Helper function to perform the search operation"""
        self.driver.get(self.url)

        # Wait for search box and input date
        searchbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_datewise_market_input_box))
        )
        searchbox.clear()
        searchbox.send_keys(self.date)

        # Wait for search button and click
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_datewise_market_search_button))
        )
        search_button.click()

    def datewise_market_indices(self):
        """Extracts datewise market indices value"""

        # Perform search operation
        self._perform_search()

        # Wait for the table to load
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, constants.xpath_datewise_market_summary_table))
        )

        # Extract table data
        datewise_market_indices_table = SeleniumDriver().extract_table_data(constants.xpath_datewise_market_summary_table)
        return datewise_market_indices_table

    def datewise_sectorwise_summary(self):
        """Extracts sector-wise summary table"""

        # Perform search operation
        self._perform_search()

        # Wait for the sector-wise summary table to load
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, xpath_datewise_sector_summary_table))
        )

        # Extract sector-wise summary table
        datewise_sectorwise_summary_table = SeleniumDriver().extract_table_data(xpath_datewise_sector_summary_table)
        return datewise_sectorwise_summary_table
