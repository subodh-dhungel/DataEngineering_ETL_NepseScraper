import psycopg2
from psycopg2 import sql
from config import get_env_variable
from logger import logger

DATABASE_URL = get_env_variable("DATABASE_URL")

class DATABASE:
    def __init__(self):
        self.connection = psycopg2.connect(DATABASE_URL)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Creates the table if it does not exist."""
        query = """
        CREATE TABLE IF NOT EXISTS scraped_data (
            id SERIAL PRIMARY KEY,
            title TEXT,
            price TEXT,
            url TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        self.cursor.execute(query)
        self.connection.commit()
    
    def insert_data(self, title, price, url):
        """Inserts scraped data into postgresql"""
        query = sql.SQL("INSERT INTO scraped_data (title, price, url) VALUES (%s,%s,%s)")
        self.cursor.execute(query, (title,price,url))
        self.connection.commit()
        logger.info(f"Inserted: {title}, {price}, {url}")
        
    def close(self):
        self.cursor.close()
        self.connection.close()