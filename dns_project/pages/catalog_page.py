from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

from base.base_class import Base
from utilities.Logger import Logger


class Catalog_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    computers_and_laptop = "//a[@class='subcategory__item ui-link ui-link_blue'][1]"
    word = "//h1[@class='subcategory__page-title']"
    laptop = "//a[@class='subcategory__item ui-link ui-link_blue'][2]"

    smartphones_and_gadgets = "//a[@class='subcategory__item ui-link ui-link_blue'][1]"
    smartphones = "//a[@class='subcategory__item ui-link ui-link_blue'][1]"

    tv = "//div[@class='subcategory__item subcategory__item_with-childs'][3]"
    televisions_and_accessories = "//div[@class='subcategory__item subcategory__item_with-childs'][3]//li[2]//a[1]"
    televisions = "//a[@class='subcategory__item ui-link ui-link_blue'][1]"

    # Required text

    cp_text_1 = "Комплектующие, компьютеры и ноутбуки"
    cp_text_2 = "Компьютеры, ноутбуки и ПО"

    cp_text_3 = "Смартфоны, планшеты и фототехника"
    cp_text_4 = "Смартфоны и гаджеты"

    # Getters

    def get_computers_and_laptop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.computers_and_laptop)))

    def get_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word)))

    def get_laptop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.laptop)))

    def get_smartphones_and_gadgets(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartphones_and_gadgets)))

    def get_smartphones(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartphones)))

    def get_tv(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv)))

    def get_televisions_and_accessories(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.televisions_and_accessories)))

    def get_televisions(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.televisions)))



    # Actions

    def click_computers_and_laptop(self):
        self.get_computers_and_laptop().click()
        print("Click Computers and Laptop Section")

    def click_laptop(self):
        self.get_laptop().click()
        print("Click Laptop Section")

    def click_smartphones_and_gadgets(self):
        self.get_smartphones_and_gadgets().click()
        print("Click Smartphones and Gadgets Section")

    def click_smartphones(self):
        self.get_smartphones().click()
        print("Click Smartphones Section")

    def click_televisions_and_accessories(self):
        self.get_televisions_and_accessories().click()
        print("Click Televisions and Accessories Section")

    def click_televisions(self):
        self.get_televisions().click()
        print("Click Televisions Section")


    # Methods

    def select_laptop(self):
        with allure.step("Select Laptop"):
            Logger.add_start_step(method="select_laptop_1")
            self.get_current_url()
            self.assert_word(self.get_word(), self.cp_text_1)
            self.click_computers_and_laptop()
            Logger.add_end_step(url=self.driver.current_url, method="select_laptop_1")
            Logger.add_start_step(method="select_laptop_2")
            self.get_current_url()
            self.assert_word(self.get_word(), self.cp_text_2)
            self.click_laptop()
            Logger.add_end_step(url=self.driver.current_url, method="select_laptop_2")

    def select_smartphone(self):
        with allure.step("Select Smartphone"):
            Logger.add_start_step(method="select_smartphone_1")
            self.get_current_url()
            self.assert_word(self.get_word(), self.cp_text_3)
            self.click_smartphones_and_gadgets()
            Logger.add_end_step(url=self.driver.current_url, method="select_smartphone_1")
            Logger.add_start_step(method="select_smartphone_2")
            self.get_current_url()
            self.assert_word(self.get_word(), self.cp_text_4)
            self.click_smartphones()
            Logger.add_end_step(url=self.driver.current_url, method="select_smartphone_2")

    def select_televisions(self):
        with allure.step("Select Televisions"):
            Logger.add_start_step(method="select_televisions_1")
            self.get_current_url()
            self.move_to_element(self.get_tv())
            self.click_televisions_and_accessories()
            Logger.add_end_step(url=self.driver.current_url, method="select_televisions_1")
            Logger.add_start_step(method="select_televisions_2")
            self.get_current_url()
            self.click_televisions()
            Logger.add_end_step(url=self.driver.current_url, method="select_televisions_2")
