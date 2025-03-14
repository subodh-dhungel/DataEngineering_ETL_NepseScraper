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

    def __new__(cls, driver_path=None, headless=True):
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

    def extract_table_data(self, xpath):
        """
        Extracts table headers and data from a given XPath.
        :param xpath: XPath of the table
        :return: Tuple (headers, data)
        """
        wait = WebDriverWait(self.driver, 10)
        max_attempts = 3

        for attempt in range(max_attempts):
            try:
                print(f"Attempt {attempt + 1}: Locating table with XPath: {xpath}")
                table = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

                # Extract headers and data directly from table
                rows = table.find_elements(By.TAG_NAME, "tr")

                # Headers: First row (th elements) or fallback to first row (td elements)
                headers = [th.text.strip() for th in rows[0].find_elements(By.TAG_NAME, "th")] or \
                          [td.text.strip() for td in rows[0].find_elements(By.TAG_NAME, "td")]

                # Data: All subsequent rows
                data = [
                    [col.text.strip() for col in row.find_elements(By.TAG_NAME, "td")]
                    for row in rows[1:]  # Skip the first row as it's the header
                ]

                return headers, data

            except StaleElementReferenceException:
                if attempt < max_attempts - 1:
                    print(f"Retrying... Attempt {attempt + 1}")
                else:
                    print("Error: Stale element reference issue!")
                    return [], []

            except TimeoutException:
                print("Error: Table not found!")
                return [], []

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
        return self.get_driver()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.driver:
            self.driver.quit()
        SeleniumDriver._instance = None
