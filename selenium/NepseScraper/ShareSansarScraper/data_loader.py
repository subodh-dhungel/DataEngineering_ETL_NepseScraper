import pandas as pd
from ShareSansarScraper import database_helper
from ShareSansarScraper.database_helper import DatabaseHelper
from ShareSansarScraper.historicaldata.historical_indices_data import HistoricalIndicesData
from datetime import datetime

class DataLoader:
    def __init__(self):
        self.db_helper = DatabaseHelper("scraperdb","scraperadmin","subodh9818")
        self.index_historical_data = HistoricalIndicesData()
        
    def load_historical_nepse_data(self,df:pd.DataFrame):
        df.drop('Signal', axis=1, inplace=True)
        
        df['scraped_at'] = datetime.now().date()
        
        df.rename(columns={
        'S.N.': 'id',
        'Index Value': 'nepse_index',
        'Absolute Change': 'absolute_change',
        'Percentage Change': 'percentage_change',
        'Turnover': 'turnover',
        'Date': 'date',
        }, inplace= True)
        
        df.set_index('id', inplace=True)
        
        # convert string columns to numeric
        cols_to_convert = ["nepse_index", "turnover"]
        df[cols_to_convert] = df[cols_to_convert].replace(',', '', regex=True).apply(pd.to_numeric, errors='coerce')
    
        df.to_csv("./indexHistoricalData.csv")
    
        #If table already exists remove it and create new one
        table_exists = self.db_helper.table_exists("historical_indices") 
        
        if table_exists:
            self.db_helper.delete_table("historical_indices")
        
        #Create table
        table_historical_data = """
            CREATE TABLE IF NOT EXISTS historical_indices (
                id SERIAL PRIMARY KEY,
                nepse_index NUMERIC,
                absolute_change NUMERIC,
                percentage_change NUMERIC,
                turnover NUMERIC,
                date DATE,
                scraped_at DATE
            );
        """
        
        self.db_helper.create_table(table_historical_data)
        
        #insert the dataframe into the table
        insert_query = """
            INSERT INTO historical_indices 
            (id,nepse_index,absolute_change, percentage_change, turnover, date, scraped_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        
        self.db_helper.insert_data(insert_query, df.reset_index().values.tolist())
        self.db_helper.close()