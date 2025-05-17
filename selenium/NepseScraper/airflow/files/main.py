from ShareSansarScraper.historicaldata.historical_charting_data import HistoricalChartData
from ShareSansarScraper.scraper import Scraper
from ShareSansarScraper.data_loader import DataLoader


def main():
    scraper = Scraper()
    
    #load data to database
    # data_loader = DataLoader()
    # historical_indices_data = HistoricalIndicesData().get_indices_historical_data("nepse", "2024-04-10", "2025-04-10")
    # data_loader.load_historical_nepse_data(historical_indices_data)
    
    # indices_historical_data = scraper.get_historical_indices_data("finance","2025-01-13", "2025-04-10")
    # print(indices_historical_data)
    
    data_loader = DataLoader()
    historical_chart_data = HistoricalChartData().get_chart_historical_data("nepse", "2024-04-10", "2025-04-10")
    data_loader.load_historical_indices_chart_data(historical_chart_data)
    
if __name__ == "__main__":
    main()
