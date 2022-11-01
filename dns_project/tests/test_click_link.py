import time
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import Main_page

@allure.description("Test Click Link")
def test_click_link(set_up, set_group):

    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\Алексей\\PycharmProjects\\resources\\chromedriver.exe', chrome_options=options)

    print("Start Test Click Link")

    mp = Main_page(driver)
    mp.click_link_1()
    mp.click_link_2()
    mp.click_link_3()
    time.sleep(3)