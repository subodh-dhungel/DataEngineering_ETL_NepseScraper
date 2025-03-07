from src.scrapers.nepse_scraper import ExampleScraper
from logger import logger 

if __name__ == "__main__":
    url = "https://www.sharesansar.com/market"
    scraper = ExampleScraper(url)
    scraper.scrape()

    logger.info("Scraping completed")
    scraper.close_driver()