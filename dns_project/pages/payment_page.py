import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.Logger import Logger


class Payment_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    hidden = "//div[@class='base-checkout-collapse-right__button_BnG']"
    product_name_payment = "//div[@class='base-checkout-products-list__item-title']"
    product_price_payment = "//div[@class='base-checkout-products-list__item-price']"

    # Required text

    payp_text_1 = '17.3" Ноутбук MSI GE77 HX Raider 12UHS-085RU серый (1шт.)'
    payp_text_2 = '315 999 ₽'

    payp_text_3 = '6.53" Смартфон Xiaomi Redmi 9A 32 ГБ серый (1шт.)'
    payp_text_4 = '5 999 ₽'

    # Getters

    def get_hidden(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.hidden)))

    def get_product_name_payment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_name_payment)))

    def get_product_price_payment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_price_payment)))

    # Actions

    def click_hidden(self):
        self.get_hidden().click()
        print("Click Hidden Window")

    # Methods

    def payment(self):
        with allure.step("Payment"):
            Logger.add_start_step(method="payment")
            time.sleep(1)
            self.get_current_url()
            self.assert_url('https://www.dns-shop.ru/checkout/')
            self.get_screenshot("payment_laptop")
            self.click_hidden()
            self.assert_word(self.get_product_name_payment(), self.payp_text_1)
            self.assert_word(self.get_product_price_payment(), self.payp_text_2)
            self.back_history()
            Logger.add_end_step(url=self.driver.current_url, method="payment")

    def payment_smartphone(self):
        with allure.step("Payment Smartphone"):
            Logger.add_start_step(method="payment_smartphone")
            time.sleep(1)
            self.get_current_url()
            self.assert_url('https://www.dns-shop.ru/checkout/')
            self.get_screenshot("payment_smartphone")
            self.click_hidden()
            self.assert_word(self.get_product_name_payment(), self.payp_text_3)
            self.assert_word(self.get_product_price_payment(), self.payp_text_4)
            self.back_history()
            Logger.add_end_step(url=self.driver.current_url, method="payment_smartphone")