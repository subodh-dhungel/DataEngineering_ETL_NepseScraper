from selenium.webdriver.support.ui import WebDriverWait
from ShareSansarScraper import constants
from ShareSansarScraper.selenium_driver import SeleniumDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import pandas as pd

class HistoricalIndicesData:
    def __init__(self):
        self.driver = SeleniumDriver().get_driver()
        self.url = constants.ss_historical_data
    
    def __perform_search(self, indices_name, fromDate, toDate):
        "search for the indices historical data by name"
        self.driver.get(self.url)
        
        #select dropdown and search for the indices
        search_dropdown = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, constants.xpath_indices_selection_element))
        )
        
        #clicking the dropdown menu.
        search_dropdown.click()
    
        #search for the indices name.
        search_input = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, constants.xpath_indices_search_input_element))
        )
        
        search_input.send_keys(indices_name)
        
        #search for the from date input field.
        date_from_input = WebDriverWait(self.driver,30).until(
            EC.presence_of_element_located((By.XPATH, constants.xpath_indices_date_from_input_element))
        )
        date_from_input.clear()
        date_from_input.send_keys(fromDate)
        
        #search for the to date input field.
        date_to_input = WebDriverWait(self.driver,30).until(
            EC.presence_of_element_located((By.XPATH, constants.xpath_indices_date_to_input_element))
        )
        date_to_input.clear()
        date_to_input.send_keys(toDate)
        
        #search for the search button.
        search_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH,constants.xpath_indices_search_button))
        )
        
        search_button.click()
        
        #wait for the table to be present in the view.
        WebDriverWait(self.driver,30).until(
            EC.presence_of_element_located((By.XPATH, constants.xpath_indices_data_table))
        )
        
    def get_indices_historical_data(self, indices_name, dateFrom, dateTo):
            """Scrape all companies from paginated table."""
            self.__perform_search(indices_name, dateFrom, dateTo)

            all_data = []
            seen_pages = set()

            while True:
                try:
                    # Re-fetch table to avoid stale elements
                    table = WebDriverWait(self.driver, 20).until(
                        EC.presence_of_element_located((By.XPATH, constants.xpath_indices_data_table))
                    )
                    rows = table.find_elements(By.TAG_NAME, "tr")

                    if not all_data:
                        headers = [th.text.strip() for th in rows[0].find_elements(By.TAG_NAME, "th")]

                    # Extract data for current page
                    page_data = [
                        [td.text.strip() for td in row.find_elements(By.TAG_NAME, "td")]
                        for row in rows[1:]
                    ]

                    # Prevent duplicate pages
                    page_hash = hash(str(page_data))
                    if page_hash in seen_pages:
                        print("Duplicate page detected, stopping pagination.")
                        break

                    seen_pages.add(page_hash)
                    all_data.extend(page_data)
                    print(f"Page {len(seen_pages)} data appended.")

                    # Re-fetch next button before checking its status
                    try:
                        next_button = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, constants.xpath_indices_next_button))
                        )
                    except TimeoutException:
                        print("Next button not found, exiting loop.")
                        break

                    # Click the next button if it's enabled, otherwise stop
                    if next_button.is_enabled():
                        next_button.click()

                        # Wait for new table data to load
                        WebDriverWait(self.driver, 20).until(
                            EC.presence_of_element_located((By.XPATH, constants.xpath_indices_data_table))
                        )
                    else:
                        print("Next button disabled, exiting loop.")
                        break
                except StaleElementReferenceException:
                    print("Stale element encountered, retrying...")
                    continue

            return pd.DataFrame(all_data, columns=headers) if all_data else pd.DataFrame()