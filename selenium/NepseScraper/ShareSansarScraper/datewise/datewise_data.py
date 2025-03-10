from ShareSansarScraper.common_selenium_operations import Operations

class DatewiseData(Operations):
    def __init__(self,url="https://www.sharesansar.com/datewise-indices", headless=True):
        super().__init__(url,headless)
    
    
    def datewise_market_indices(self):
        """Extracts datewise market indices value"""
        #locate the presence of searchbox and enter the text to search
        #locate the presence of button and click the button
        #extract the datewise market indices table

        
    def datewise_sectorwise_summary(self):
        """Extract sectorwise summary table"""
        #locate the presence of searchbox and enter the text to search
        #locate the presence of button and click the button 
        #extract the datewise market indices table
    
    