import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cart_page import Cart_page
from pages.catalog_page import Catalog_page
from pages.catalog_product_selection_page import Catalog_product_selection_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page
from pages.product_page import Product_page

@pytest.mark.run(order=1)
@allure.description("Test Buy Product 1")
def test_buy_product_1(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\Алексей\\PycharmProjects\\resources\\chromedriver.exe', chrome_options=options)

    print("Start Test Buy Product 1")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_computers_catalog()

    cp = Catalog_page(driver)
    cp.select_laptop()

    cpsp = Catalog_product_selection_page(driver)
    cpsp.selection_laptop_checkbox()
    cpsp.select_product_laptop()

    pp = Product_page(driver)
    pp.add_to_cart_product_laptop()
    pp.go_to_cart()

    crtp = Cart_page(driver)
    crtp.product_confirmation()

    payp = Payment_page(driver)
    payp.payment()

    crtp.clean_cart()

@pytest.mark.run(order=2)
@allure.description("Test Buy Product 2")
def test_buy_product_2(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\Алексей\\PycharmProjects\\resources\\chromedriver.exe', chrome_options=options)

    print("Start Test Buy Product 2")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_smartphone_catalog()

    cp = Catalog_page(driver)
    cp.select_smartphone()

    cpsp = Catalog_product_selection_page(driver)
    cpsp.selection_smartphone_checkbox()
    cpsp.add_cart_product_smartphone()

    crtp = Cart_page(driver)
    crtp.product_confirmation_smartphone()

    payp = Payment_page(driver)
    payp.payment_smartphone()

    crtp.clean_cart()