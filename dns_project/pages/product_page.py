from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

from base.base_class import Base
from utilities.Logger import Logger


class Product_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    product_laptop_name_product = "//h1[@class='product-card-top__title']"
    product_laptop_price_product = "//div[@class='product-card-top__buy']//*[@class='product-buy__price']"
    add_to_cart_passive = "//div[@class='product-card-top__buy']//button[2]"
    add_to_cart_active = "//div[@class='product-card-top__buy']//*[@class='button-ui buy-btn button-ui_brand']"
    cart = "//span[@class='cart-link__price']"

    # Required text

    pp_text_1 = '17.3" Ноутбук MSI GE77 HX Raider 12UHS-085RU серый'
    pp_text_2 = '315 999 ₽'

    # Getters

    def get_product_laptop_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_laptop_name_product)))

    def get_product_laptop_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_laptop_price_product)))

    def get_add_to_cart_passive(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_passive)))

    def get_add_to_cart_active(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_active)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    # Actions

    def click_add_to_cart_active(self):
        self.get_add_to_cart_active().click()
        print("Click Add to Cart")

    def click_cart(self):
        self.get_cart().click()
        print("Click Cart")


    # Methods

    def add_to_cart_product_laptop(self):
        with allure.step("Add to Cart Product Laptop"):
            Logger.add_start_step(method="add_to_cart_product_laptop")
            self.get_current_url()
            self.get_screenshot("product_laptop")
            self.assert_word(self.get_product_laptop_name_product(), self.pp_text_1)
            self.assert_word(self.get_product_laptop_price_product(), self.pp_text_2)
            self.move_to_element(self.get_add_to_cart_passive())
            self.click_add_to_cart_active()
            Logger.add_end_step(url=self.driver.current_url, method="add_to_cart_product_laptop")

    def go_to_cart(self):
        with allure.step("Go to Cart"):
            Logger.add_start_step(method="go_to_cart")
            self.click_cart()
            Logger.add_end_step(url=self.driver.current_url, method="go_to_cart")




