from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

from base.base_class import Base
from utilities.Logger import Logger


class Login_page(Base):

    url = 'https://www.dns-shop.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    login_button = "//div[@class='user-menu']"
    login_button_1 = "//*[@id='user-menu']/div/div[3]/div[2]/div/div[1]/button"
    login_password_button = "//*[@id='user-menu']/div[1]/div[2]/modal/div/div/div/div[4]/div[2]/div/div"
    user_name_click = "//div[@class='form-entry-with-password__input']"
    user_name = "//input[@autocomplete='username']"
    password_click = "//div[@class='form-entry-with-password__password']"
    password = "//input[@autocomplete='current-password']"
    login_button_2 = "//*[@id='user-menu']/div[1]/div[2]/modal/div/div/div/div[6]/div/button"
    main_word = "//span[@class='title']"

    # Getters

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_login_button_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button_1)))

    def get_login_password_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_password_button)))

    def get_user_name_click(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name_click)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password_click(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_click)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button_2)))

    # Actions

    def click_login_button(self):
        self.get_login_button().click()
        print("Click Login Button")

    def click_login_button_1(self):
        self.get_login_button_1().click()
        print("Click Login Button 1")

    def click_login_password_button(self):
        self.get_login_password_button().click()
        print("Click Login Password Button")

    def click_user_name(self):
        self.get_user_name_click().click()
        print("Click Input Username")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input Username")

    def click_password(self):
        self.get_password_click().click()
        print("Click Input Password")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input Password")

    def click_login_button_2(self):
        self.get_login_button_2().click()
        print("Click Login Button 2")

    # Methods

    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_login_button()
            self.click_login_button_1()
            self.click_login_password_button()
            self.click_user_name()
            self.input_user_name("te5tinguser@yandex.ru")
            self.click_password()
            self.input_password("Testinguser1")
            self.click_login_button_2()
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
