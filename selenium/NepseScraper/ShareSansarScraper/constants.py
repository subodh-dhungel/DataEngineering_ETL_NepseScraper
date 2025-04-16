#urls
from re import X


ss_marketpage_url = "https://www.sharesansar.com/market"
ss_datewise_market_url = "https://www.sharesansar.com/datewise-indices"
ss_companypage_url = "https://www.sharesansar.com/company-list"
ss_historical_data = "https://www.sharesansar.com/indices-sub-indices"
ss_historical_chart_data = "https://www.sharesansar.com/index-history-data"

#constant for current day market indices table jasto nepseIndex, float, senfloat, etc.
xpath_current_day_indices_table = "/html/body/div[2]/div/section[2]/div[3]/div/div[3]/div[1]/div/div[1]/div[2]/table"

#constant for current day market summary table jasto todays total turnover, volume, number of scrips traded
xpath_market_summary_table = "/html/body/div[2]/div/section[2]/div[3]/div/div[3]/div[2]/div/div[1]/div[2]/table"
xpath_sectorwise_summary_table = "/html/body/div[2]/div/section[2]/div[3]/div/div[5]/div[1]/div/div[1]/div[2]/table"
xpath_top_gainers_table = "/html/body/div[2]/div/section[2]/div[3]/div/div[7]/div[1]/div/div[1]/div[2]/table"
xpath_top_losers_table = "/html/body/div[2]/div/section[2]/div[3]/div/div[7]/div[2]/div/div[1]/div[2]/table"
xpath_top_turnover_table = "/html/body/div[2]/div/section[2]/div[3]/div/div[7]/div[3]/div/div[1]/div[2]/table"
xpath_top_traded_shares_table = "/html/body/div[2]/div/section[2]/div[3]/div/div[9]/div[1]/div/div[1]/div[2]/table"
xpath_top_traded_transactions = "/html/body/div[2]/div/section[2]/div[3]/div/div[9]/div[2]/div/div[1]/div[2]/table"
xpath_top_brokers = "/html/body/div[2]/div/section[2]/div[3]/div/div[9]/div[3]/div/div[1]/div[2]/table"

#constant for datewise market summary
xpath_datewise_market_input_box = "/html/body/div[2]/div/section[2]/div[3]/div/div/div/div/div[1]/form/div[1]/input"
xpath_datewise_market_search_button = "/html/body/div[2]/div/section[2]/div[3]/div/div/div/div/div[1]/form/div[2]/button"
xpath_datewise_market_summary_table = "/html/body/div[2]/div/section[2]/div[3]/div/div/div/div/div[1]/div[4]/div/div/table[1]"
xpath_datewise_sector_summary_table = "/html/body/div[2]/div/section[2]/div[3]/div/div/div/div/div[1]/div[4]/div/div/table[2]"

#constant for companies
xpath_companies_selection_element = "/html/body/div[2]/div/section[2]/div[3]/div/div/div/div/div[1]/form/div[1]/span/span[1]/span/span[1]"
xpath_companies_input_element = "/html/body/span/span/span[1]/input"
xpath_companies_search_button = "/html/body/div[2]/div/section[2]/div[3]/div/div/div/div/div[1]/form/div[2]/button"
xpath_companies_data_table = "/html/body/div[2]/div/section[2]/div[3]/div/div/div/div/div[1]/div[4]/div/table"
xpath_next_button = "/html/body/div[2]/div/section[2]/div[3]/div/div/div/div/div[1]/div[4]/div/div[5]/a[2]"
xpath_paginated_span = "/html/body/div[2]/div/section[2]/div[3]/div/div/div/div/div[1]/div[4]/div/div[5]/span"

#constants for historical indices data.
xpath_indices_selection_element = "/html/body/div[2]/div/section[2]/div[3]/div/div/div/div/div[1]/form/div[1]/span/span[1]/span"
xpath_indices_search_input_element = "/html/body/span/span/span[1]/input"
xpath_indices_date_from_input_element = "/html/body/div[2]/div/section[2]/div[3]/div/div/div/div/div[1]/form/div[2]/input"
xpath_indices_date_to_input_element = "/html/body/div[2]/div/section[2]/div[3]/div/div/div/div/div[1]/form/div[3]/input"
xpath_indices_search_button = "/html/body/div[2]/div/section[2]/div[3]/div/div/div/div/div[1]/form/div[4]/button"
xpath_indices_data_table = "/html/body/div[2]/div/section[2]/div[3]/div/div/div/div/div[1]/div[4]/div/table"
xpath_indices_next_button = "/html/body/div[2]/div/section[2]/div[3]/div/div/div/div/div[1]/div[4]/div/div[5]/a[2]"
xpath_indices_paginated_span = "/html/body/div[2]/div/section[2]/div[3]/div/div/div/div/div[1]/div[4]/div/div[5]/span"

#constants for historical charting data
xpath_chart_selection_element = '//*[@id="frm_datewise"]/div[1]/span/span[1]/span'
xpath_chart_search_input_element = '/html/body/span/span/span[1]/input'
xpath_chart_date_from_input_element = '//*[@id="fromDate"]'
xpath_chart_date_to_input_element = '//*[@id="toDate"]'
xpath_chart_search_button = '//*[@id="btn_indxhis_submit"]'
xpath_chart_data_table = '//*[@id="myTable"]'
xpath_chart_next_button = '//*[@id="myTable_next"]'
xpath_chart_paginated_span = '//*[@id="myTable_paginate"]/span'
