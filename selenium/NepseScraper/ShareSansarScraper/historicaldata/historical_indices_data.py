from selenium.webdriver.support.ui import WebDriverWait
from ShareSansarScraper import constants
from ShareSansarScraper.selenium_driver import SeleniumDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import pandas as pd

class HistoricalIndicesData:
    def __init__(self):
        self.url = constants.ss_historical_data

    def __perform_search(self, driver, indices_name, fromDate, toDate):
        """Search for the indices historical data by name"""
        driver.get(self.url)
        
        # Click dropdown
        search_dropdown = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, constants.xpath_indices_selection_element))
        )
        search_dropdown.click()
    
        # Enter indices name
        search_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, constants.xpath_indices_search_input_element))
        )
        search_input.send_keys(indices_name)
        
        # Set date from
        date_from_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, constants.xpath_indices_date_from_input_element))
        )
        date_from_input.clear()
        date_from_input.send_keys(fromDate)
        
        # Set date to
        date_to_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, constants.xpath_indices_date_to_input_element))
        )
        date_to_input.clear()
        date_to_input.send_keys(toDate)
        
        # Click search
        search_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, constants.xpath_indices_search_button))
        )
        search_button.click()

        # Wait for data table
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, constants.xpath_indices_data_table))
        )

    def get_indices_historical_data(self, indices_name, dateFrom, dateTo):
        """Scrape all companies from paginated table"""
        with SeleniumDriver() as selenium_driver:
            driver = selenium_driver.get_driver()

            self.__perform_search(driver, indices_name, dateFrom, dateTo)

            all_data = []
            seen_pages = set()
            headers = []

            while True:
                try:
                    # Get table
                    table = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.XPATH, constants.xpath_indices_data_table))
                    )
                    rows = table.find_elements(By.TAG_NAME, "tr")

                    if not headers:
                        headers = [th.text.strip() for th in rows[0].find_elements(By.TAG_NAME, "th")]

                    # Get table rows
                    page_data = [
                        [td.text.strip() for td in row.find_elements(By.TAG_NAME, "td")]
                        for row in rows[1:]
                    ]

                    page_hash = hash(str(page_data))
                    if page_hash in seen_pages:
                        print("Duplicate page detected, stopping pagination.")
                        break

                    seen_pages.add(page_hash)
                    all_data.extend(page_data)
                    print(f"Page {len(seen_pages)} data appended.")

                    # Click next button
                    try:
                        next_button = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, constants.xpath_indices_next_button))
                        )
                    except TimeoutException:
                        print("Next button not found, exiting loop.")
                        break

                    if next_button.is_enabled():
                        next_button.click()

                        # Wait for next page to load
                        WebDriverWait(driver, 20).until(
                            EC.presence_of_element_located((By.XPATH, constants.xpath_indices_data_table))
                        )
                    else:
                        print("Next button disabled, exiting loop.")
                        break
                except StaleElementReferenceException:
                    print("Stale element encountered, retrying...")
                    continue

            return pd.DataFrame(all_data, columns=headers) if all_data else pd.DataFrame()
