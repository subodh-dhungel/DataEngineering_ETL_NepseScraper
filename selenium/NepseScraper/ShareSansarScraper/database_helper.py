import psycopg2
from psycopg2 import sql

class DatabaseHelper:
    def __init__(self, db_name, user, password, host='localhost', port=5432):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        self.cursor = None
        self.connect()
        
    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.conn.cursor()
            print("Connected to PostgreSQL database.")
        except Exception as e:
            print("Failed to connect to database: ", e)

    def create_table(self, table_sql):
        try:
            self.cursor.execute(table_sql)
            self.conn.commit()
            print("Table created successfully...")
        except Exception as e:
            self.conn.rollback()
            print("Failed to create table:", e)

    def insert_data(self, query, data):
        try:
            self.cursor.executemany(query, data)
            self.conn.commit()
            print("Data inserted successfully.")
        except Exception as e:
            self.conn.rollback()
            print("Failed to insert data:", e)

    def fetch_all(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            self.conn.rollback()
            print("Failed to fetch data:", e)
            return []

    def delete_data(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            print("Data deleted successfully.")
        except Exception as e:
            self.conn.rollback()
            print("Failed to delete data:", e)

    def delete_table(self, table_name):
        try:
            query = sql.SQL("DROP TABLE IF EXISTS {}").format(sql.Identifier(table_name))
            self.cursor.execute(query)
            self.conn.commit()
            print(f"Table '{table_name}' deleted successfully.")
        except Exception as e:
            self.conn.rollback()
            print(f"Failed to delete table '{table_name}':", e)
        
    def table_exists(self, table_name):
        """Helper method to check whether or not
        table exists or not in the database."""
        try:
            # Query to check if the table exists in the 'public' schema
            self.cursor.execute("""
                SELECT EXISTS (
                    SELECT 1
                    FROM information_schema.tables
                    WHERE table_name = %s
                    AND table_schema = 'public'
                );
            """, (table_name,))
            exists = self.cursor.fetchone()[0]
            if exists:
                return True
            else:
                return False
        except Exception as e:
            self.conn.rollback()
            print("Failed to check if table exists:", e)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Database connection closed...")
