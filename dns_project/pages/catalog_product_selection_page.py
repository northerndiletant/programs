
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

from base.base_class import Base
from utilities.Logger import Logger


class Catalog_product_selection_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    rating_checkbox_laptop = "//div[@data-id='rating']"
    price_1_checkbox_laptop = "//div[@data-id='price']//*[@class='ui-checkbox ui-checkbox_list'][6]"
    manufacturer_1_checkbox_laptop = "//div[@data-id='brand']//*[@class='ui-checkbox ui-checkbox_list'][16]"
    gaming_laptop_open_laptop = "//div[@data-id='f[p3q]']//*[@class='ui-link ui-collapse__link_left ui-collapse__link ui-collapse__link_list']"
    gaming_laptop_checkbox_laptop = "//div[@data-id='f[p3q]']//*[@class='ui-checkbox ui-checkbox_list'][1]"
    operating_system_open_laptop = "//div[@data-id='f[65f]']//*[@class='ui-link ui-collapse__link_left ui-collapse__link ui-collapse__link_list']"
    operating_system_checkbox_laptop = "//div[@data-id='f[65f]']//*[@class='ui-checkbox ui-checkbox_list'][2]"
    core_open_laptop = "//div[@data-id='f[66r]']//*[@class='ui-link ui-collapse__link_left ui-collapse__link ui-collapse__link_list']"
    core_checkbox_laptop = "//div[@data-id='f[66r]']//*[@class='ui-checkbox ui-checkbox_list'][4]"
    processor_manufacturer_open_laptop = "//div[@data-id='f[66f]']//*[@class='ui-link ui-collapse__link_left ui-collapse__link ui-collapse__link_list']"
    processor_manufacturer_checkbox_laptop = "//div[@data-id='f[66f]']//*[@class='ui-checkbox ui-checkbox_list'][3]"
    apply_button = "//button[@data-role='filters-submit']"
    result_filter = "//div[@class='top-filters__picked-wrap']"
    product_laptop_catalog = "//div[@data-code='5047128']"
    product_laptop_name_catalog = "//div[@data-code='5047128']//*[@class='catalog-product__name ui-link ui-link_black']"
    product_laptop_price_catalog = "//div[@data-code='5047128']//*[@class='product-buy__price']"

    info_page_1 = "//h1[@class='title']"

    rating_checkbox_smartphone = "//div[@data-id='rating']"
    price_checkbox_smartphone = "//div[@data-id='price']//*[@class='ui-checkbox ui-checkbox_list'][2]"
    manufacturer_checkbox_smartphone = "//div[@data-id='brand']//*[@class='ui-checkbox ui-checkbox_list'][30]"
    battery_capacity = "//div[@data-id='fr[9af]']//*[@class='ui-link ui-collapse__link_left ui-collapse__link ui-collapse__link_list']"
    battery_capacity_input_1 = "//input[@placeholder='от 1 550']"
    battery_capacity_input_2 = "//input[@placeholder='до 15 600']"
    product_smartphone_catalog = "//div[@data-code='1678777']"
    product_smartphone_name_catalog = "//div[@data-code='1678777']//*[@class='catalog-product__name ui-link ui-link_black']"
    product_smartphone_price_catalog = "//div[@data-code='1678777']//*[@class='product-buy__price product-buy__price_active']"
    add_cart_smartphone = "//div[@data-code='1678777']/*/button[2]"
    go_to_cart_catalog = "//span[@class='base-ui-button-v2__text'][text()='В корзину']"

    rating_checkbox_televisions = "//div[@data-id='rating']"
    price_checkbox_televisions_1 = "//div[@data-id='price']//*[@class='ui-checkbox ui-checkbox_list'][2]"
    tv_1 = "//div[@data-code='5349630']"
    tv_name_1 = "//div[@data-code='5349630']//*[@class='catalog-product__name ui-link ui-link_black']"
    tv_price_1 = "//div[@data-code='5349630']//*[@class='product-buy__price']"
    compare_checkbox_1 = "//div[@data-code='5349630']//*[@class='ui-checkbox']"
    reset_button = "//button[@data-role='filters-reset']"
    price_checkbox_televisions_2 = "//div[@data-id='price']//*[@class='ui-checkbox ui-checkbox_list'][3]"
    tv_2 = "//div[@data-code='5017386']"
    tv_name_2 = "//div[@data-code='5017386']//*[@class='catalog-product__name ui-link ui-link_black']"
    tv_price_2 = "//div[@data-code='5017386']//*[@class='product-buy__price']"
    compare_checkbox_2 = "//div[@data-code='5017386']//*[@class='ui-checkbox']"
    compare_button_catalog = "//span[@class='compare-link__lbl']"

    # Required text

    cpsp_text_1 = '17.3" Ноутбук MSI GE77 HX Raider 12UHS-085RU серый [Quad HD 2K (2560x1440), IPS, Intel Core i9-12900HX, ядра: 8 + 8, RAM 32 ГБ, SSD 2000 ГБ, GeForce RTX 3080 Ti для ноутбуков 16 ГБ, Windows 11 Home Single Language]'
    cpsp_text_2 = '315 999 ₽'

    cpsp_text_3 = '8K телевизоры'

    cpsp_text_4 = '6.53" Смартфон Xiaomi Redmi 9A 32 ГБ серый [8x(2 ГГц), 2 Гб, 2 SIM, IPS, 1600x720, камера 13 Мп, 4G, GPS, 5000 мА*ч]'
    cpsp_text_5 = '5 999 ₽\n6 999'

    cpsp_text_6 = '32" (81 см) Телевизор LED Candy Uno 32 черный [HD, 1366x768, Wi-Fi, 60 Гц, Android TV, HDMI х 3, USB х 2]'
    cpsp_text_7 = '15 499 ₽'
    cpsp_text_8 = '50" (127 см) Телевизор LED DEXP U50G9000C/G серый [4K UltraHD, 3840x2160, Wi-Fi, 60 Гц, Яндекс.ТВ, HDMI х 3, USB х 2]'
    cpsp_text_9 = '25 499 ₽'


    # Getters

    def get_rating_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.rating_checkbox_laptop)))

    def get_price_1_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.price_1_checkbox_laptop)))

    def get_manufacturer_1_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.manufacturer_1_checkbox_laptop)))

    def get_gaming_laptop_open(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.gaming_laptop_open_laptop)))

    def get_gaming_laptop_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.gaming_laptop_checkbox_laptop)))

    def get_operating_system_open(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.operating_system_open_laptop)))

    def get_operating_system_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.operating_system_checkbox_laptop)))

    def get_core_open(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.core_open_laptop)))

    def get_core_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.core_checkbox_laptop)))

    def get_processor_manufacturer_open(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.processor_manufacturer_open_laptop)))

    def get_processor_manufacturer_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.processor_manufacturer_checkbox_laptop)))

    def get_apply_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apply_button)))

    def get_result_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.result_filter)))

    def get_product_laptop_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_laptop_catalog)))

    def get_product_laptop_name_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_laptop_name_catalog)))

    def get_product_laptop_price_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_laptop_price_catalog)))

    def get_info_page_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.info_page_1)))

    def get_rating_checkbox_smartphone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.rating_checkbox_smartphone)))

    def get_price_checkbox_smartphone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_checkbox_smartphone)))

    def get_manufacturer_checkbox_smartphone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.manufacturer_checkbox_smartphone)))

    def get_battery_capacity(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.battery_capacity)))

    def get_battery_capacity_input_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.battery_capacity_input_1)))

    def get_battery_capacity_input_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.battery_capacity_input_2)))

    def get_product_smartphone_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_smartphone_catalog)))

    def get_product_smartphone_name_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_smartphone_name_catalog)))

    def get_product_smartphone_price_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_smartphone_price_catalog)))

    def get_add_cart_smartphone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_cart_smartphone)))

    def get_go_to_cart_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_catalog)))

    def get_rating_checkbox_televisions(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.rating_checkbox_televisions)))

    def get_price_checkbox_televisions_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_checkbox_televisions_1)))

    def get_tv_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv_1)))

    def get_tv_name_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv_name_1)))

    def get_tv_price_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv_price_1)))

    def get_compare_checkbox_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.compare_checkbox_1)))

    def get_reset_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.reset_button)))

    def get_price_checkbox_televisions_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_checkbox_televisions_2)))

    def get_tv_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv_2)))

    def get_tv_name_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv_name_2)))

    def get_tv_price_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv_price_2)))

    def get_compare_checkbox_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.compare_checkbox_2)))

    def get_compare_button_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.compare_button_catalog)))

    # Actions

    def click_rating_checkbox(self):
        self.get_rating_checkbox().click()
        print("Click Rating Checkbox")

    def click_price_1_checkbox(self):
        self.get_price_1_checkbox().click()
        print("Click Price Checkbox")

    def click_manufacturer_1_checkbox(self):
        self.get_manufacturer_1_checkbox().click()
        print("Click Manufacturer Checkbox")

    def click_gaming_laptop_open(self):
        self.get_gaming_laptop_open().click()
        print("Click Gaming Laptop")

    def click_gaming_laptop_checkbox(self):
        self.get_gaming_laptop_checkbox().click()
        print("Click Gaming Laptop Checkbox")

    def click_operating_system_open(self):
        self.get_operating_system_open().click()
        print("Click Operating System")

    def click_operating_system_checkbox(self):
        self.get_operating_system_checkbox().click()
        print("Click Operating System Checkbox")

    def click_core_open(self):
        self.get_core_open().click()
        print("Click Core")

    def click_core_checkbox(self):
        self.get_core_checkbox().click()
        print("Click Core Checkbox")

    def click_processor_manufacturer_open(self):
        self.get_processor_manufacturer_open().click()
        print("Click Processor Manufacturer")

    def click_processor_manufacturer_checkbox(self):
        self.get_processor_manufacturer_checkbox().click()
        print("Click Processor Manufacturer Checkbox")

    def click_apply_button(self):
        self.get_apply_button().click()
        print("Click Apply Button")

    def click_product_laptop_name_catalog(self):
        self.get_product_laptop_name_catalog().click()
        print("Click Product laptop")

    def click_rating_checkbox_smartphone(self):
        self.get_rating_checkbox().click()
        print("Click Rating Checkbox")

    def click_price_checkbox_smartphone(self):
        self.get_price_checkbox_smartphone().click()
        print("Click Price Checkbox")

    def click_manufacturer_checkbox_smartphone(self):
        self.get_manufacturer_checkbox_smartphone().click()
        print("Click Manufacturer Checkbox")

    def click_battery_capacity(self):
        self.get_battery_capacity().click()
        print("Click Battery Capacity")

    def click_battery_capacity_input_1(self):
        self.get_battery_capacity_input_1().click()
        print("Click Input Battery Capacity")

    def click_battery_capacity_input_2(self):
        self.get_battery_capacity_input_2().click()
        print("Click Input Battery Capacity")

    def input_battery_capacity_input_1(self):
        self.get_battery_capacity_input_1().send_keys("2000")
        print("Input Battery Capacity")

    def input_battery_capacity_input_2(self):
        self.get_battery_capacity_input_2().send_keys("10000")
        print("Input Battery Capacity")

    def click_add_cart_smartphone(self):
        self.get_add_cart_smartphone().click()
        print("Click Add to Cart")

    def click_go_to_cart_catalog(self):
        self.get_go_to_cart_catalog().click()
        print("Click Cart")

    def click_rating_checkbox_televisions(self):
        self.get_rating_checkbox_televisions().click()
        print("Click Rating Checkbox")

    def click_price_checkbox_televisions_1(self):
        self.get_price_checkbox_televisions_1().click()
        print("Click Price Checkbox")

    def click_compare_checkbox_1(self):
        self.get_compare_checkbox_1().click()
        print("Click Compare Checkbox")

    def click_reset_button(self):
        self.get_reset_button().click()
        print("Click Reset Button")

    def click_price_checkbox_televisions_2(self):
        self.get_price_checkbox_televisions_2().click()
        print("Click Price Checkbox")

    def click_compare_checkbox_2(self):
        self.get_compare_checkbox_2().click()
        print("Click Compare Checkbox")

    def click_compare_button_catalog(self):
        self.get_compare_button_catalog().click()
        print("Click Compare Button")

    # Methods

    def selection_laptop_checkbox(self):
        with allure.step("Selection Laptop Checkbox"):
            Logger.add_start_step(method="selection_laptop_checkbox")
            self.get_current_url()
            self.page_down_and_home_body()
            self.move_to_element(self.get_rating_checkbox())
            self.click_rating_checkbox()
            self.move_to_element(self.get_price_1_checkbox())
            self.click_price_1_checkbox()
            self.move_to_element(self.get_manufacturer_1_checkbox())
            self.click_manufacturer_1_checkbox()
            self.move_to_element(self.get_gaming_laptop_open())
            self.click_gaming_laptop_open()
            self.move_to_element(self.get_gaming_laptop_checkbox())
            self.click_gaming_laptop_checkbox()
            self.move_to_element(self.get_operating_system_open())
            self.click_operating_system_open()
            self.move_to_element(self.get_operating_system_checkbox())
            self.click_operating_system_checkbox()
            self.move_to_element(self.get_core_open())
            self.click_core_open()
            self.move_to_element(self.get_core_checkbox())
            self.click_core_checkbox()
            self.move_to_element(self.get_processor_manufacturer_open())
            self.click_processor_manufacturer_open()
            self.move_to_element(self.get_processor_manufacturer_checkbox())
            self.click_processor_manufacturer_checkbox()
            self.move_to_element(self.get_apply_button())
            self.click_apply_button()
            self.move_to_element(self.get_result_filter())
            self.get_screenshot("laptop_filters")
            Logger.add_end_step(url=self.driver.current_url, method="selection_laptop_checkbox")

    def select_product_laptop(self):
        with allure.step("Select Product Laptop"):
            Logger.add_start_step(method="select_product_laptop")
            self.move_to_element(self.get_product_laptop_catalog())
            self.assert_word(self.get_product_laptop_name_catalog(), self.cpsp_text_1)
            self.assert_word(self.get_product_laptop_price_catalog(), self.cpsp_text_2)
            self.click_product_laptop_name_catalog()
            Logger.add_end_step(url=self.driver.current_url, method="select_product_laptop")

    def check_menu_catalog(self):
        with allure.step("Check Menu Catalog"):
            Logger.add_start_step(method="check_menu_catalog")
            self.get_current_url()
            self.assert_word(self.get_info_page_1(), self.cpsp_text_3)
            self.get_screenshot("catalog")
            Logger.add_end_step(url=self.driver.current_url, method="check_menu_catalog")

    def selection_smartphone_checkbox(self):
        with allure.step("Selection Smartphone Checkbox"):
            Logger.add_start_step(method="selection_smartphone_checkbox")
            self.get_current_url()
            self.page_down_and_home_body()
            self.move_to_element(self.get_rating_checkbox_smartphone())
            self.click_rating_checkbox_smartphone()
            self.move_to_element(self.get_price_checkbox_smartphone())
            self.click_price_checkbox_smartphone()
            self.move_to_element(self.get_manufacturer_checkbox_smartphone())
            self.click_manufacturer_checkbox_smartphone()
            self.move_to_element(self.get_battery_capacity())
            self.click_battery_capacity()
            self.move_to_element(self.get_battery_capacity_input_1())
            self.click_battery_capacity_input_1()
            self.input_battery_capacity_input_1()
            self.move_to_element(self.get_battery_capacity_input_2())
            self.click_battery_capacity_input_2()
            self.input_battery_capacity_input_2()
            self.move_to_element(self.get_apply_button())
            self.click_apply_button()
            self.move_to_element(self.get_result_filter())
            self.get_screenshot("smartphone_filters")
            Logger.add_end_step(url=self.driver.current_url, method="selection_smartphone_checkbox")

    def add_cart_product_smartphone(self):
        with allure.step("Add Cart Product Smartphone"):
            Logger.add_start_step(method="add_cart_product_smartphone")
            self.move_to_element(self.get_product_smartphone_catalog())
            self.assert_word(self.get_product_smartphone_name_catalog(), self.cpsp_text_4)
            self.assert_word(self.get_product_smartphone_price_catalog(), self.cpsp_text_5)
            self.move_to_element(self.get_add_cart_smartphone())
            self.click_add_cart_smartphone()
            self.click_go_to_cart_catalog()
            Logger.add_end_step(url=self.driver.current_url, method="add_cart_product_smartphone")

    def add_to_compare(self):
        with allure.step("Add to Compare"):
            Logger.add_start_step(method="add_to_compare")
            self.get_current_url()
            self.page_down_and_home_body()
            self.move_to_element(self.get_rating_checkbox_televisions())
            self.click_rating_checkbox_televisions()
            self.move_to_element(self.get_price_checkbox_televisions_1())
            self.click_price_checkbox_televisions_1()
            self.move_to_element(self.get_apply_button())
            self.click_apply_button()
            self.move_to_element(self.get_result_filter())
            self.move_to_element(self.get_tv_1())
            self.assert_word(self.get_tv_name_1(), self.cpsp_text_6)
            self.assert_word(self.get_tv_price_1(), self.cpsp_text_7)
            self.click_compare_checkbox_1()
            self.move_to_element(self.get_reset_button())
            self.click_reset_button()
            self.move_to_element(self.get_rating_checkbox_televisions())
            self.click_rating_checkbox_televisions()
            self.move_to_element(self.get_price_checkbox_televisions_2())
            self.click_price_checkbox_televisions_2()
            self.move_to_element(self.get_apply_button())
            self.click_apply_button()
            self.move_to_element(self.get_result_filter())
            self.move_to_element(self.get_tv_2())
            self.assert_word(self.get_tv_name_2(), self.cpsp_text_8)
            self.assert_word(self.get_tv_price_2(), self.cpsp_text_9)
            self.click_compare_checkbox_2()
            self.click_compare_button_catalog()
            Logger.add_end_step(url=self.driver.current_url, method="add_to_compare")
