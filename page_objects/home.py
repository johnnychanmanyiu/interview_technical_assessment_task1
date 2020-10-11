from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from time import sleep

class HomeScreen(object):

    base_url = 'https://crypto.com/exchange'
    CRO_MARKET = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/div[3]')
    CRO_USDC = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div/div/ul/li[29]/div[7]')

    def __init__(self, driver: webdriver):
        self.driver = driver
    
    def get_url(self):
        url = self.base_url
        return url

    def open(self) -> 'HomeScreen':
        self.driver.get(self.get_url())
        self.driver.maximize_window()
        # wait page fully loaded
        sleep(5)
        return self

    def find(self,locator):
        return self.driver.find_element(*locator)
    
    def accept_cookies(self):
        try:
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[4]/div[2]/div/button').click()
        except:
            pass