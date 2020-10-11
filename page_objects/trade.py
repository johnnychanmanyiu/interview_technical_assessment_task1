from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from page_objects.home import HomeScreen

class TradingScreen(HomeScreen):

    # for layout
    TRADING_VIEW = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div[1]/div')
    ORDER_LIST_BOX = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div[2]/div')
    TRADING_HISTORY = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[2]/div[1]')
    TRADING_BOX = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[2]/div[2]')
    DROP_DOWN_MENU = (By.XPATH, '//*[@id="app"]/div/header/div/div[2]/div[2]/div/div/div')
    # for login
    TRADE_BOX_LOGIN = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/button')
    # for order history
    ORDER_HISTORY = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]')
    # for trading box
    TRADING_BOX_PRICE = (By.XPATH, '/html/body/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div/input')
    TRADING_BOX_AMOUNT = (By.XPATH, '/html/body/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[3]/div/input')
    TRADING_BOX_TOTAL = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[5]/div/div/span[1]')

    def __init__(self, driver: webdriver):
        super().__init__(driver)


