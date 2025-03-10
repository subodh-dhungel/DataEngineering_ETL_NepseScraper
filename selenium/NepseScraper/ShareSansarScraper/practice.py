from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SeleniumDriver:
    def __init__(self,path,url):
        self.service=Service(executable_path=path)
        self.driver=webdriver.Chrome(service=self.service)
        self.url=url
        self.driver.implicitly_wait(10)

    def element_to_be_clickable(self,by_type,by_value,time_to_wait:int=10):
        try:
            return WebDriverWait(self.driver,time_to_wait).until(EC.element_to_be_clickable((by_type,by_value)))
        except TimeoutError as e:
            print("element is unclickable")
            return None

    def click_element(self,by_type,by_value):
        element=self.element_to_be_clickable(by_type,by_value)
        if element is not None:
            element.click()

    def presence_of_element(self,by_type,by_value:str,time_to_wait:int=10):
        try:
            return WebDriverWait(self.driver,time_to_wait).until(EC.presence_of_all_elements_located((by_type, by_value)))
        except TimeoutError as e:
            print("element is not present within the time :",e)
            return None

    def find_elements(self,by_type,by_value):
        return self.presence_of_element(by_type,by_value)
    

    def enter_text(self,by_type,by_value,text_value):
        element=self.presence_of_element(by_type,by_value)
        for x in element:
            x.send_keys(text_value+Keys.ENTER)

    def get_data(self,by_type,by_value,array_data_structure,attribute=None):
        elements=self.presence_of_element(by_type,by_value)
        for element in elements:
            if attribute is not None:           
                array_data_structure.append(element.text)

            else:
                array_data_structure.append(element.get_attribute(attribute))
