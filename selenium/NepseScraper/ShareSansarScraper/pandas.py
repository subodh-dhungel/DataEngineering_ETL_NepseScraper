import pandas as pd

class PandasOperations:
    """Handles dataframe creation, formatting, and printing"""
    
    @staticmethod
    def create_dataframe(headers, data):
        """Creates a pandas DataFrame from headers and data."""
        if not data:
            print("No data available")
            return None
        
        df = pd.DataFrame(data, columns=headers)
        return df
    
    @staticmethod
    def print_dataframe(df, title="Dataframe"):
        if df is not None:
            print(f"{title}")
            print(df)
            print("\n" + "="*50 + "\n")
        else:
            print(f"{title} is empty.")
