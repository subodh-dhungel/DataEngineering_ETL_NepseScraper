from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

class SeleniumDriver:
    """Singleton class and context manager for Selenium WebDriver."""
    _instance = None

    def __new__(cls, driver_path=None, headless=True):
        if cls._instance is None:
            cls._instance = super(SeleniumDriver, cls).__new__(cls)
            cls._instance._initialize_driver(driver_path, headless)
        return cls._instance

    def _initialize_driver(self, driver_path, headless):
        """Initializes the WebDriver with given options."""
        self.service = Service(driver_path or os.getenv("SELENIUM_DRIVER_PATH"))
        self.options = webdriver.ChromeOptions()
        if headless:
            self.options.add_argument("--headless")
            self.options.add_argument("--disable-gpu")
            self.options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def get_driver(self):
        return self.driver

    def quit(self):
        if self.driver:
            self.driver.quit()

    # Context manager methods
    def __enter__(self):
        return self.get_driver()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()
