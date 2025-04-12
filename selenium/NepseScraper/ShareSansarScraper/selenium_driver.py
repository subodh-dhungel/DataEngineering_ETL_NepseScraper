from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

class SeleniumDriver:
    """Singleton class and context manager for Selenium WebDriver."""
    _instance = None

    def __new__(cls, driver_path=None, headless=False):
        if cls._instance is None:
            cls._instance = super(SeleniumDriver, cls).__new__(cls)
            cls._instance._initialize_driver(driver_path, headless)
        return cls._instance

    def _initialize_driver(self, driver_path, headless):
        """Initializes the WebDriver."""
        self.service = Service(driver_path or os.getenv("SELENIUM_DRIVER_PATH"))
        self.options = webdriver.ChromeOptions()

        # Headless mode setup
        if headless:
            self.options.add_argument("--headless")

        # Anti-detection settings
        self.options.add_argument("--disable-infobars")  
        self.options.add_argument("--disable-dev-shm-usage")  
        self.options.add_argument("--no-sandbox")  
        self.options.add_argument("--disable-gpu")  
        self.options.add_argument("--disable-features=IsolateOrigins,site-per-process")  

        # Start driver
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.implicitly_wait(10)  

    def get_driver(self):
        return self.driver

    def quit(self):
        """Closes the WebDriver and resets the singleton instance."""
        if self.driver:
            self.driver.quit()
            SeleniumDriver._instance = None 

    def extract_table_data(self, xpath , url):
        """Extract table data using an XPath."""
        driver = self.get_driver()
        
        try:
            driver.get(url)
            # Wait for the table element to be present
            table = WebDriverWait(self.get_driver(), 10).until(
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


    def locate_element(self, identifier: str, identifier_type, wait_time: int = 30):
        """Waits for an element to be present and returns it."""
        try:
            print(f"Locating element by {identifier_type}: {identifier}")
            element = WebDriverWait(self.get_driver(), wait_time).until(
                EC.presence_of_element_located((identifier_type, identifier))
            )
            return element
        except TimeoutException:
            print(f"Element with {identifier} not found within {wait_time} seconds.")
            return None

    # Context manager methods
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.driver:
            self.driver.quit()
        SeleniumDriver._instance = None