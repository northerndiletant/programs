import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.Logger import Logger


class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    product_laptop_name_cart = "//a[@target='_self']"
    product_laptop_price_cart = "//div[@class='price']"
    confirm_button = "//button[@id='buy-btn-main']"

    delete_product = "//p[@class='remove-button__title']"

    product_smartphone_name_cart = "//a[@target='_self']"
    product_smartphone_price_cart = "//div[@class='price']//*[@class='price__current']"

    # Required text

    crtp_text_1 = '17.3" Ноутбук MSI GE77 HX Raider 12UHS-085RU серый'
    crtp_text_2 = '315 999 ₽'

    crtp_text_3 = '6.53" Смартфон Xiaomi Redmi 9A 32 ГБ серый'
    crtp_text_4 = '5 999 ₽'

    # Getters

    def get_product_laptop_name_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_laptop_name_cart)))

    def get_product_laptop_price_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_laptop_price_cart)))

    def get_confirm_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_button)))

    def get_delete_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_product)))

    def get_product_smartphone_name_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_smartphone_name_cart)))

    def get_product_smartphone_price_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_smartphone_price_cart)))

    # Actions

    def click_confirm_button(self):
        self.get_confirm_button().click()
        print("Click Confirm Button")

    def click_delete_product(self):
        self.get_delete_product().click()
        print("Cart Clean")

    # Methods

    def product_confirmation(self):
        with allure.step("Product Confirmation"):
            Logger.add_start_step(method="product_confirmation")
            self.get_current_url()
            self.get_screenshot("cart_laptop")
            self.assert_word(self.get_product_laptop_name_cart(), self.crtp_text_1)
            self.assert_word(self.get_product_laptop_price_cart(), self.crtp_text_2)
            time.sleep(1)
            self.click_confirm_button()
            Logger.add_end_step(url=self.driver.current_url, method="product_confirmation")

    def clean_cart(self):
        with allure.step("Clean Cart"):
            Logger.add_start_step(method="clean_cart")
            self.click_delete_product()
            self.get_screenshot("empty_cart")
            Logger.add_end_step(url=self.driver.current_url, method="clean_cart")

    def product_confirmation_smartphone(self):
        with allure.step("Product Confirmation Smartphone"):
            Logger.add_start_step(method="product_confirmation_smartphone")
            self.get_current_url()
            self.get_screenshot("cart_smartphone")
            self.assert_word(self.get_product_smartphone_name_cart(), self.crtp_text_3)
            self.assert_word(self.get_product_smartphone_price_cart(), self.crtp_text_4)
            time.sleep(1)
            self.click_confirm_button()
            Logger.add_end_step(url=self.driver.current_url, method="product_confirmation_smartphone")


