import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.Logger import Logger


class Compare_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    catalog_button = "//div[@class='base-ui-button base-ui-button_brand']"
    tv_name_1_compare = "//div[@class='products-slider__item'][1]//*[@class='base-ui-link base-ui-link_black']"
    tv_price_1_compare = "//div[@class='products-slider__item'][1]//*[@class='product-min-price__current']"
    tv_name_2_compare = "//div[@class='products-slider__item'][2]//*[@class='base-ui-link base-ui-link_black']"
    tv_price_2_compare = "//div[@class='products-slider__item'][2]//*[@class='product-min-price__current']"
    delete_all = "//span[@class='clear-app__link']"

    # Required text

    comp_text_1 = '50" (127 см) Телевизор LED DEXP U50G9000C/G серый'
    comp_text_2 = '25 499 ₽'
    comp_text_3 = '32" (81 см) Телевизор LED Candy Uno 32 черный'
    comp_text_4 = '15 499 ₽'

    # Getters

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_tv_name_1_compare(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv_name_1_compare)))

    def get_tv_price_1_compare(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv_price_1_compare)))

    def get_tv_name_2_compare(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv_name_2_compare)))

    def get_tv_price_2_compare(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv_price_2_compare)))

    def get_delete_all(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_all)))

    # Actions

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click Catalog Button")

    def click_delete_all(self):
        self.get_delete_all().click()
        print("Compare List Clean")

    # Methods

    def catalog_button_compare(self):
        with allure.step("Catalog Button Compare"):
            Logger.add_start_step(method="catalog_button_compare")
            self.get_current_url()
            self.get_screenshot("compare_empty")
            self.click_catalog_button()
            Logger.add_end_step(url=self.driver.current_url, method="catalog_button_compare")

    def compare_list(self):
        with allure.step("Compare List"):
            Logger.add_start_step(method="compare_list")
            self.get_current_url()
            self.get_screenshot("compare_list")
            self.assert_word(self.get_tv_name_1_compare(), self.comp_text_1)
            self.assert_word(self.get_tv_price_1_compare(), self.comp_text_2)
            self.assert_word(self.get_tv_name_2_compare(), self.comp_text_3)
            self.assert_word(self.get_tv_price_2_compare(), self.comp_text_4)
            self.click_delete_all()
            self.get_screenshot("clean_compare")
            Logger.add_end_step(url=self.driver.current_url, method="compare_list")





