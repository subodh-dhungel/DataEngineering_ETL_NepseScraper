from ShareSansarScraper.current_day_data import CurrentDayData
import pandas as pd

def main():
    scraper = CurrentDayData(headless=True)  # Set headless=False for debugging
    headers, table_data = scraper.current_market_indices()

    if table_data:
        df = pd.DataFrame(table_data, columns=headers if headers else None)
        print(df)

    scraper.close_driver()

if __name__ == "__main__":
    main()
