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
from page_objects.login import LoginScreen

scenarios('../feature/B-Check_trading_page.feature')

@fixture()
def browser():
    browser = webdriver.Chrome()
    sleep(5)
    yield browser
    browser.close()
    browser.quit()

#B01
@given('I am on CRO/USDC trading page')
def is_on_CRO_USDC_trading_page(browser):
    HomeScreen(browser).open()
    HomeScreen(browser).accept_cookies()
    HomeScreen(browser).find(HomeScreen.CRO_MARKET).click()
    try:
        HomeScreen(browser).find(HomeScreen.CRO_USDC).click()
    except:
        sleep(5)
        HomeScreen(browser).find(HomeScreen.CRO_USDC).click()
    assert 'CRO/USDC' in TradingScreen(browser).find(TradingScreen.DROP_DOWN_MENU).text

@then('I should have trading view')
def should_have_trading_view(browser):
    TradingScreen(browser).find(TradingScreen.TRADING_VIEW)

@then('I should have order list box')
def should_have_order_list_box(browser):
    TradingScreen(browser).find(TradingScreen.ORDER_LIST_BOX)

@then('I should have trading history')
def should_have_trading_histroy(browser):
    TradingScreen(browser).find(TradingScreen.TRADING_HISTORY)

@then('I should have trading box')
def should_have_trading_box(browser):
    TradingScreen(browser).find(TradingScreen.TRADING_BOX)

#B02
@when('I click login on trading box')
def click_login(browser):
    TradingScreen(browser).find(TradingScreen.TRADE_BOX_LOGIN).click()

@then('I should be on login page')
def should_be_on_login_page(browser):
    LoginScreen(browser).find(LoginScreen.LOGIN_EMAIL)

#B03
@given('I login with <email> and <password>')
def login_with_email_and_password(browser,email,password):
    # require test data
    pass

@when('I click order history')
def click_order_history(browser):
    TradingScreen(browser).find(TradingScreen.ORDER_HISTORY).click()

@then('I should have order history')
def should_have_order_history(browser):
    # require test data
    pass

#B04
@when('I input <price> and <amount>')
def input_price_and_amount(browser,price,amount):
    sleep(5)
    TradingScreen(browser).find(TradingScreen.TRADING_BOX_PRICE).clear()
    TradingScreen(browser).find(TradingScreen.TRADING_BOX_PRICE).send_keys(price)
    TradingScreen(browser).find(TradingScreen.TRADING_BOX_AMOUNT).send_keys(amount)

@then('I should have <total>')
def should_have_total(browser,total):
    assert total in TradingScreen(browser).find(TradingScreen.TRADING_BOX_TOTAL).text