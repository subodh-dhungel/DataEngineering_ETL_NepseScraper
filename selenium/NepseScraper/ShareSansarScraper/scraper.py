# Get data for the current market indices
# Get data for the current market summary
# Get data for the sectorwise market summary
# Get data for the datewise market summary
# Get the data for the sectorwise summary
# Get the data for the historical indices summary data

from ShareSansarScraper.current_day.current_day_data import CurrentDayData
from ShareSansarScraper.datewise.datewise_data import DatewiseData
from ShareSansarScraper.pandas import PandasOperations


class Scraper:
    def __init__(self):
        self.current_day_data = CurrentDayData()
    
    def get_current_market_indices(self):
        """Scraper Method to get the current day market data."""
        indices_headers, indices_data = self.current_day_data.current_market_indices()
        if indices_data:
            indices_df = PandasOperations.create_dataframe(indices_headers,indices_data)
            return indices_df
        else:
            # logging required after logger module implemented
            pass
    
    def get_current_market_summary(self):
        """Scraper method to get the current market summary."""
        summary_headers, summary_data = self.current_day_data.current_market_summary()
        if summary_data:
            summary_df = PandasOperations.create_dataframe(summary_headers,summary_data)
            return summary_df
        else:
            # logging required if needed
            pass
    
    def get_sectorwise_market_summary(self):
        """Scraper method to get the sectorwise market summary."""
        sector_headers, sector_data = self.current_day_data.current_sectorwise_summary()
        if sector_data:
            sector_df = PandasOperations.create_dataframe(sector_headers,sector_data)
            return sector_df
        else:
            #logging required if needed
            pass
        
    def get_datewise_market_indices(self, date:str):
        """Scrper method to get the datewise market summary using date"""
        datewise_market_data = DatewiseData(date)
        result = datewise_market_data.datewise_market_indices()
        headers,data = result
        if data:
            df = PandasOperations.create_dataframe(headers,data)
            return df
        else:
            #logging required if needed
            pass
    
    def get_datewise_sectorwise_summary(self, date:str):
        datewise_market_data = DatewiseData(date)
        result = datewise_market_data.datewise_sectorwise_summary()
        headers, data = result
        if data:
            df = PandasOperations.create_dataframe(headers,data)
            return df
        else:
            #logging required if needed
            pass
    