from ShareSansarScraper import constants
from ShareSansarScraper.constants import *
from ShareSansarScraper.selenium_driver import SeleniumDriver

class CurrentDayData:
    """Scraper for extracting table data from Sharesansar Market page."""

    def __init__(self):
        self.url = constants.ss_marketpage_url

    #Test Pass
    def current_market_indices(self):
        with SeleniumDriver() as driver:
            return driver.extract_table_data(xpath_current_day_indices_table, self.url)

    def current_market_summary(self):
        with SeleniumDriver() as driver:
            return driver.extract_table_data(xpath_market_summary_table, self.url)

    def current_sectorwise_summary(self):
        with SeleniumDriver() as driver:
            return driver.extract_table_data(xpath_sectorwise_summary_table, self.url)

    def current_top_gainers(self):
        with SeleniumDriver() as driver:
            return driver.extract_table_data(xpath_top_gainers_table, self.url)

    def current_top_losers(self):
        with SeleniumDriver() as driver:
            return driver.extract_table_data(xpath_top_losers_table, self.url)

    def current_top_turnover(self):
        with SeleniumDriver() as driver:
            return driver.extract_table_data(xpath_top_turnover_table, self.url)

    def current_top_traded_shares(self):
        with SeleniumDriver() as driver:
            return driver.extract_table_data(xpath_top_traded_shares_table, self.url)

    def current_top_traded_transactions(self):
        with SeleniumDriver() as driver:
            return driver.extract_table_data(xpath_top_traded_transactions, self.url)

    def current_top_brokers(self):
        with SeleniumDriver() as driver:
            return driver.extract_table_data(xpath_top_brokers, self.url)
