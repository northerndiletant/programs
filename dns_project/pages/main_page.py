
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from base.base_class import Base
from utilities.Logger import Logger


class Main_page(Base):

    url = 'https://www.dns-shop.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    computers_catalog = "//a[@href='/catalog/17aa72ab16404e77/komplektuyushhie-kompyutery-i-noutbuki/']"

    selector_menu_catalog_1 = "//a[@href='/catalog/17a8bfb516404e77/tv-i-multimedia/']"
    selector_menu_catalog_2 = "//a[@href='/catalog/17a8ae4916404e77/televizory/']"
    selector_menu_catalog_3 = "//a[@href='/catalog/recipe/a929745586a086a1/8k/']"

    smartphone_catalog = "//a[@href='/catalog/17a890dc16404e77/smartfony-planshety-i-fototexnika/']"

    compare_button = "//span[@class='compare-link__lbl']"

    link_1 = "//div[@class='site-logo__wrapper']//*[@href='https://club.dns-shop.ru/']"
    link_2 = "//a[@href='https://www.dns-tech.ru/']"
    link_3 = "//a[@href='https://dnsgroup.ru']"

    # Getters

    def get_computers_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.computers_catalog)))

    def get_selector_menu_catalog_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selector_menu_catalog_1)))

    def get_selector_menu_catalog_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selector_menu_catalog_2)))

    def get_selector_menu_catalog_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selector_menu_catalog_3)))

    def get_smartphone_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartphone_catalog)))

    def get_compare_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.compare_button)))

    def get_link_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_1)))

    def get_link_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_2)))

    def get_link_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_3)))

    # Actions

    def click_computers_catalog(self):
        self.get_computers_catalog().click()
        print("Click Computers Section")

    def click_selector_menu_catalog_3(self):
        self.get_selector_menu_catalog_3().click()
        print("Click Selector Menu")

    def click_smartphone_catalog(self):
        self.get_smartphone_catalog().click()
        print("Click Smartphone Section")

    def click_compare_button(self):
        self.get_compare_button().click()
        print("Click Compare Button")

    def click_get_link_1(self):
        self.get_link_1().click()
        print("Click link")

    def click_get_link_2(self):
        self.get_link_2().click()
        print("Click link")

    def click_get_link_3(self):
        self.get_link_3().click()
        print("Click link")


    # Methods

    def select_computers_catalog(self):
        with allure.step("Select Computers Catalog"):
            Logger.add_start_step(method="select_computers_catalog")
            self.get_current_url()
            try:
                self.click_computers_catalog()
            except StaleElementReferenceException:
                print("StaleElementReferenceException")
                self.driver.refresh()
                self.click_computers_catalog()
            Logger.add_end_step(url=self.driver.current_url, method="select_computers_catalog")


    def select_product_in_menu(self):
        with allure.step("Select Product in Menu"):
            Logger.add_start_step(method="select_product_in_menu")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.move_to_element(self.get_selector_menu_catalog_1())
            self.move_to_element(self.get_selector_menu_catalog_2())
            self.click_selector_menu_catalog_3()
            Logger.add_end_step(url=self.driver.current_url, method="select_product_in_menu")

    def select_smartphone_catalog(self):
        with allure.step("Select Smartphone Catalog"):
            Logger.add_start_step(method="select_smartphone_catalog")
            self.get_current_url()
            try:
                self.click_smartphone_catalog()
            except StaleElementReferenceException:
                print("StaleElementReferenceException")
                self.driver.refresh()
                self.click_smartphone_catalog()
            Logger.add_end_step(url=self.driver.current_url, method="select_smartphone_catalog")

    def compare(self):
        with allure.step("Compare"):
            Logger.add_start_step(method="compare")
            self.get_current_url()
            try:
                self.click_compare_button()
            except StaleElementReferenceException:
                print("StaleElementReferenceException")
                self.driver.refresh()
                self.click_compare_button()
            Logger.add_end_step(url=self.driver.current_url, method="compare")

    def click_link_1(self):
        with allure.step("Click Link 1"):
            Logger.add_start_step(method="click_link_1")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.move_to_element(self.get_link_1())
            self.click_get_link_1()
            self.get_current_url()
            self.assert_url("https://club.dns-shop.ru/")
            self.get_screenshot("link_1")
            self.back_history()
            self.back_history()
            Logger.add_end_step(url=self.driver.current_url, method="click_link_1")

    def click_link_2(self):
        with allure.step("Click Link 2"):
            Logger.add_start_step(method="click_link_2")
            self.get_current_url()
            self.move_to_element(self.get_link_2())
            self.click_get_link_2()
            self.get_current_url()
            self.assert_url("https://www.dns-tech.ru/")
            self.get_screenshot("link_2")
            self.back_history()
            Logger.add_end_step(url=self.driver.current_url, method="click_link_2")

    def click_link_3(self):
        with allure.step("Click Link 3"):
            Logger.add_start_step(method="click_link_3")
            self.get_current_url()
            self.move_to_element(self.get_link_3())
            self.click_get_link_3()
            self.get_current_url()
            self.assert_url("https://dnsgroup.ru/ru")
            self.get_screenshot("link_3")
            self.back_history()
            Logger.add_end_step(url=self.driver.current_url, method="click_link_3")
