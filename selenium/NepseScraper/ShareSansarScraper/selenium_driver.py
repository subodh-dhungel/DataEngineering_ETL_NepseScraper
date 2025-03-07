from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

class SeleniumDriver:
    """Singleton class to initialize and manage Selenium WebDriver."""
    _instance = None

    def __new__(cls, driver_path="/usr/bin/chromedriver", headless=True):
        if cls._instance is None:
            cls._instance = super(SeleniumDriver, cls).__new__(cls)
            cls._instance.driver = cls._initialize_driver(driver_path, headless)
        return cls._instance

    @staticmethod
    def _initialize_driver(driver_path, headless):
        """Initializes the Selenium WebDriver."""
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")

        service = Service(driver_path)
        return webdriver.Chrome(service=service, options=options)
