from selenium import webdriver
from pytest import fixture
from time import sleep
from pytest_bdd import (
    scenarios,
    given,
    when,
    then,
    parsers
)

from page_objects.home import HomeScreen
from page_objects.trade import TradingScreen

scenarios('../feature/A-Reach_trading_page.feature')

@fixture()
def browser():
    browser = webdriver.Chrome()
    sleep(5)
    yield browser
    browser.close()
    browser.quit()

#A01
@given('I go to homepage')
def go_to_homepage(browser):
    HomeScreen(browser).open()

@then('I should be on homepage')
def should_be_on_homepage(browser):
    HomeScreen(browser).find(HomeScreen.CRO_MARKET)

#A02
@given('I am on homepage')
def is_on_homepage(browser):
    HomeScreen(browser).open()
    HomeScreen(browser).accept_cookies()
    HomeScreen(browser).find(HomeScreen.CRO_MARKET)

@when('I click CRO Markets')
def click_CRO_Markets(browser):
    HomeScreen(browser).find(HomeScreen.CRO_MARKET).click()

@when('I click CRO/USDC')
def click_CRO_USDC(browser):
    try:
        HomeScreen(browser).find(HomeScreen.CRO_USDC).click()
    except:
        sleep(5)
        HomeScreen(browser).find(HomeScreen.CRO_USDC).click()

@then('I should be on CRO/USDC trading page')
def should_be_on_trading_page(browser):
    # wait for page fully loaded
    sleep(5)
    TradingScreen(browser).find(TradingScreen.TRADE_BOX_LOGIN)
