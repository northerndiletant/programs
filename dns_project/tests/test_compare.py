import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.catalog_page import Catalog_page
from pages.catalog_product_selection_page import Catalog_product_selection_page
from pages.compare_page import Compare_page
from pages.login_page import Login_page
from pages.main_page import Main_page

@allure.description("Test Compare")
def test_compare(set_up, set_group):

    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\Алексей\\PycharmProjects\\resources\\chromedriver.exe', chrome_options=options)

    print("Start Test Compare")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.compare()

    comp = Compare_page(driver)
    comp.catalog_button_compare()

    cp = Catalog_page(driver)
    cp.select_televisions()

    cpsp = Catalog_product_selection_page(driver)
    cpsp.add_to_compare()

    comp.compare_list()