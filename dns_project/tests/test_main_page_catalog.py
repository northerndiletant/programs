import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.catalog_product_selection_page import Catalog_product_selection_page
from pages.main_page import Main_page

@allure.description("Test Main Page Catalog")
def test_main_page_catalog(set_up, set_group):

    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\Алексей\\PycharmProjects\\resources\\chromedriver.exe', chrome_options=options)

    print("Start Test Main Page Catalog")

    mp = Main_page(driver)
    mp.select_product_in_menu()

    cpsp = Catalog_product_selection_page(driver)
    cpsp.check_menu_catalog()