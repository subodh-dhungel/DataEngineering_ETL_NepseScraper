from ShareSansarScraper import constants
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ShareSansarScraper.selenium_driver import SeleniumDriver
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import pandas as pd

class ListedCompanies:
    def __init__(self):
        self.driver = SeleniumDriver().get_driver()
        self.url = constants.ss_companypage_url
        
    def __perform_search(self, sector_name):
        """Search for the sector by name."""
        self.driver.get(self.url)

        # Select dropdown and search for sector
        search_dropdown = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, constants.xpath_companies_selection_element))
        )
        search_dropdown.click()

        search_input = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, constants.xpath_companies_input_element))
        )
        search_input.send_keys(sector_name)

        search_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, constants.xpath_companies_search_button))
        )
        search_button.click()

        # Wait for table to appear
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, constants.xpath_companies_data_table))
        )
        
    def get_companies_by_sector(self, sector_name):
        """Scrape all companies from paginated table."""
        self.__perform_search(sector_name)

        all_data = []
        seen_pages = set()  # Track visited pages

        while True:
            try:
                # Re-fetch table to avoid stale elements
                table = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, constants.xpath_companies_data_table))
                )
                rows = table.find_elements(By.TAG_NAME, "tr")

                if not all_data:  # Fetch headers only once
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
                        EC.presence_of_element_located((By.XPATH, constants.xpath_next_button))
                    )
                except TimeoutException:
                    print("Next button not found, exiting loop.")
                    break

                # Click the next button if it's enabled, otherwise stop
                if next_button.is_enabled():
                    next_button.click()

                    # Wait for new table data to load
                    WebDriverWait(self.driver, 20).until(
                        EC.presence_of_element_located((By.XPATH, constants.xpath_companies_data_table))
                    )
                else:
                    print("Next button disabled, exiting loop.")
                    break  # Stop pagination
            except StaleElementReferenceException:
                print("Stale element encountered, retrying...")
                continue

        return pd.DataFrame(all_data, columns=headers) if all_data else pd.DataFrame()
