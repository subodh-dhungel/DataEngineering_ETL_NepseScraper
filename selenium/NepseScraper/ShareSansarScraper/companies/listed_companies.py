from ShareSansarScraper import constants
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from ShareSansarScraper.selenium_driver import SeleniumDriver
import pandas as pd
import time

class ListedCompanies:
    def __init__(self):
        self.driver = SeleniumDriver().get_driver()
        self.url = constants.ss_companypage_url
        
    def __perform_search(self, sector_name):
        """Search for the sector by name."""
        
        self.driver.get(constants.ss_companypage_url)
        
        # Search for the sector search dropdown menu
        search_dropdown = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, constants.xpath_selection_element))
        )
        
        # Clicking the dropdown menu after searching
        search_dropdown.click()
        
        # Searching the sectorwise input element after clicking the button.
        search_input = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, constants.xpath_companies_input_element))
        )
        
        # Sending the sector name to search in the text input.
        search_input.send_keys(sector_name)

        # Searching the sector search button in the page
        search_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, constants.xpath_companies_search_button))
        )
        
        # Clicking the searchh button after the search is completed.
        search_button.click()
        time.sleep(5)
        
    def get_companies_by_sector(self, sector_name):
        """Get companies for a specific sector."""
        self.__perform_search(sector_name)
        
        # Get sectorwise companies  
        try:
            table = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, constants.xpath_companies_data_table))
            )
            
            rows = table.find_elements(By.TAG_NAME, "tr")
            headers = [th.text.strip() for th in rows[0].find_elements(By.TAG_NAME, "th")]
            data = [
                [td.text.strip() for td in row.find_elements(By.TAG_NAME, "td")]
                for row in rows[1:]
            ]

            df = pd.DataFrame(data, columns=headers)
            return df

        except TimeoutException:
            print("Error: Table not found!")
            return pd.DataFrame()  
