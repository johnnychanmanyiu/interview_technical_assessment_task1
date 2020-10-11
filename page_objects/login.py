from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from page_objects.home import HomeScreen

class LoginScreen(HomeScreen):

    LOGIN_EMAIL = (By.XPATH, '//*[@id="user_email"]')
    LOGIN_PASSWORD = (By.XPATH, '//*[@id="user_password"]')

    def __init__(self, driver: webdriver):
        super().__init__(driver)


