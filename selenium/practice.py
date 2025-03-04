from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("subodh raj dhungel"+ Keys.ENTER)

time.sleep(50)
driver.quit()
