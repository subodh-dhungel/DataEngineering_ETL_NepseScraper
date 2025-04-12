from ShareSansarScraper.scraper import Scraper


def main():
    scraper = Scraper()
    
    #load data to database
    # data_loader = DataLoader()
    # historical_indices_data = HistoricalIndicesData().get_indices_historical_data("nepse", "2024-04-10", "2025-04-10")
    # data_loader.load_historical_nepse_data(historical_indices_data)
    
    current_market_indices = scraper.get_datewise_sectorwise_summary("2025-04-10")
    print(current_market_indices)
    
if __name__ == "__main__":
    main()
