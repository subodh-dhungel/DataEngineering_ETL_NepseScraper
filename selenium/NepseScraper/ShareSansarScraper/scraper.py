import logging
from ShareSansarScraper.historicaldata.historical_indices_data import HistoricalIndicesData
from ShareSansarScraper.pandas import PandasOperations
from ShareSansarScraper.current_day.current_day_data import CurrentDayData
from ShareSansarScraper.datewise.datewise_data import DatewiseData
from ShareSansarScraper.historicaldata.historical_charting_data import HistoricalChartData

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Scraper:
    def __init__(self):
        self.current_day_data = CurrentDayData()

    def get_current_market_indices(self):
        """Scraper Method to get the current day market data."""
        try:
            indices_headers, indices_data = self.current_day_data.current_market_indices()
            if indices_data:
                return PandasOperations.create_dataframe(indices_headers, indices_data)
            else:
                logger.warning("No data found for current market indices.")
                return None
        except Exception as e:
            logger.error(f"Error scraping current market indices: {e}")
            return None
    
    def get_current_market_summary(self):
        """Scraper method to get the current market summary."""
        try:
            summary_headers, summary_data = self.current_day_data.current_market_summary()
            if summary_data:
                return PandasOperations.create_dataframe(summary_headers, summary_data)
            else:
                logger.warning("No data found for current market summary.")
                return None
        except Exception as e:
            logger.error(f"Error scraping current market summary: {e}")
            return None
    
    def get_sectorwise_market_summary(self):
        """Scraper method to get the sectorwise market summary."""
        try:
            sector_headers, sector_data = self.current_day_data.current_sectorwise_summary()
            if sector_data:
                return PandasOperations.create_dataframe(sector_headers, sector_data)
            else:
                logger.warning("No data found for sectorwise market summary.")
                return None
        except Exception as e:
            logger.error(f"Error scraping sectorwise market summary: {e}")
            return None

    def get_datewise_market_indices(self, date: str):
        """Scraper method to get the datewise market summary using date."""
        try:
            datewise_market_data = DatewiseData(date)
            headers, data = datewise_market_data.datewise_market_indices()
            if data:
                return PandasOperations.create_dataframe(headers, data)
            else:
                logger.warning("No data found for datewise market indices.")
                return None
        except Exception as e:
            logger.error(f"Error scraping datewise market indices: {e}")
            return None

    def get_datewise_sectorwise_summary(self, date: str):
        """Scraper method to get the datewise sectorwise summary."""
        try:
            datewise_market_data = DatewiseData(date)
            headers, data = datewise_market_data.datewise_sectorwise_summary()
            if data:
                return PandasOperations.create_dataframe(headers, data)
            else:
                logger.warning("No data found for datewise sectorwise summary.")
                return None
        except Exception as e:
            logger.error(f"Error scraping datewise sectorwise summary: {e}")
            return None

    def get_historical_indices_data(self,indices_name, date_from, date_to):
        """Scraper method to get the historical indices data"""
        try:
            historical_indices_data = HistoricalIndicesData()
            df = historical_indices_data.get_indices_historical_data(indices_name, date_from, date_to)
            if not df.empty:
                df.to_csv(f"/generatedCSV/{indices_name} historical data.csv")
                return df
            else:
                logger.warning(f"No data found for {indices_name} historical data")
                return None
            
        except Exception as e:
            logger.error(f"Error scraping historical indices data: {e}")
            return None

    def get_historical_chart_data(self,indices_name, date_from, date_to):
        """Scraper method to get the historical chart data"""
        try:
            historical_indices_data = HistoricalChartData()
            df = historical_indices_data.get_chart_historical_data(indices_name, date_from, date_to)
            if not df.empty:
                df.to_csv(f"./{indices_name} charting data.csv", index=False)
                return df
            else:
                logger.warning(f"No data found for {indices_name} historical data")
                return None
            
        except Exception as e:
            logger.error(f"Error scraping historical indices data: {e}")
            return None