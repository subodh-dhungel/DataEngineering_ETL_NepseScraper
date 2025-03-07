from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()

driver.get("https://www.sharesansar.com/")


try:
    market_overview_elem = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/section[1]/div/div/div/ul/li[4]/ul/li[1]/a"))
    )
    market_overview_elem.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/section[2]/div[3]/div/div[3]/div[1]/div/div[1]')) 
    )
    
finally:
    driver.quit()