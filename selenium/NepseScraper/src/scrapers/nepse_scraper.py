from selenium.webdriver.common.by import By
from scrapers.base_scraper import Database
from logger import logger 
from scrapers.base_scraper import BaseScraper

class NepseScraper(BaseScraper):
    """Scraper for a specific website using selenium"""
    """Yo file j huna pani sakcha"""
    def scrape(self):
        """Extracts product data using selenium. """
        self.load_page()
        db = Database()