from ShareSansarScraper.current_day.current_day_data import CurrentDayData
import pandas as pd

def main():
    scraper = CurrentDayData(headless=True) 
    
    # Get data for the current market indices
    # indices_headers, indices_data = scraper.current_market_indices()
    # if indices_data:
    #     indices_df = pd.DataFrame(indices_data, columns=indices_headers if indices_headers else None)
    #     print("Current Market Indices:")
    #     print(indices_df)
    #     print("\n" + "="*50 + "\n")

    # Get data for the current market summary
    # summary_headers, summary_data = scraper.current_market_summary()
    # if summary_data:
    #     summary_df = pd.DataFrame(summary_data, columns=summary_headers if summary_headers else None)
    #     print("Current Market Summary:")
    #     print(summary_df)

    # Get data for the sectorwise market summary
    sector_headers, sector_data = scraper.current_sectorwise_summary()
    if sector_data:
        sector_df = pd.DataFrame(sector_data, columns=sector_headers if sector_headers else None)
        print("Current Market sector: ")
        print(sector_df)

if __name__ == "__main__":
    main()
