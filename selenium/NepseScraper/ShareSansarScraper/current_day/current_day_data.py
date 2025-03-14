from ShareSansarScraper.constants import *
from ShareSansarScraper.common_selenium_operations import Operations
from ShareSansarScraper.selenium_driver import SeleniumDriver

class CurrentDayData(SeleniumDriver):
    """Scraper for extracting table data from Sharesansar Market page."""
    
    def __init__(self, url="https://www.sharesansar.com/market", headless=False):
        super().__init__()

    def current_market_indices(self):
        """Extracts current market indices data from sharesansaar"""
        return self.extract_table_data(xpath_current_day_indices_table)

    def current_market_summary(self):
        """Extracts market summary data from sharesansaar"""
        return self.extract_table_data(xpath_market_summary_table)

    def current_sectorwise_summary(self):
        """Extracts sectorwise summary data from sharesansaar"""
        return self.extract_table_data(xpath_sectorwise_summary_table)
    
    def current_top_gainers(self):
        """Extract daily top gainers data from sharesansar"""
        return self.extract_table_data(xpath_top_gainers_table)
    
    def current_top_losers(self):
        """Extract daily top losers data from sharesansar"""
        return self.extract_table_data(xpath_top_losers_table)
    
    def current_top_turnover(self):
        """Extract daily top turnover data from sharesansar"""
        return self.extract_table_data(xpath_top_turnover_table)
    
    def current_top_traded_shares(self):
        """Extract daily top traded shares data from sharesansar"""
        return self.extract_table_data(xpath_top_traded_shares_table)
    
    def current_top_traded_transactions(self):
        """Extract daily top traded transactions data from sharesansar"""
        return self.extract_table_data(xpath_top_traded_transactions)
    
    def current_top_brokers(self):
        """Extract daily top broker buy sell data from sharesansar"""
        return self.extract_table_data(xpath_top_brokers)
    
