import psycopg2

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
            print("Failed to create table:", e)

    def insert_data(self, query, data):
        try:
            self.cursor.executemany(query, data)
            self.conn.commit()
            print("Data inserted successfully.")
        except Exception as e:
            print("Failed to insert data:", e)

    def fetch_all(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
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
            print("Failed to delete data:", e)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Database connection closed...")
