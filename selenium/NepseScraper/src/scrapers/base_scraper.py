from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import get_env_variable
from logger import logger

class SeleniumDriver:
    """Singleton class to initialize and manage Selenium WebDriver."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SeleniumDriver, cls).__new__(cls)
            cls._instance.driver = cls._initialize_driver()
        return cls._instance

    @staticmethod
    def _initialize_driver():
        """Initializes the Selenium WebDriver."""
        driver_path = get_env_variable("SELENIUM_DRIVER_PATH")
        service = Service(driver_path)
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        
        logger.info("Initializing Selenium WebDriver")
        return webdriver.Chrome(service=service, options=options)

class BaseScraper:
    """Base scraper class for Selenium-based scrapers."""
    def __init__(self, url):
        self.url = url
        self.driver = SeleniumDriver().driver

    def load_page(self):
        """Loads the webpage using Selenium."""
        logger.info(f"Loading page: {self.url}")
        self.driver.get(self.url)

    def close_driver(self):
        """Closes the Selenium WebDriver."""
        logger.info("Closing WebDriver")
        self.driver.quit()
