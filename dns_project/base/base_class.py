import datetime
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method Get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current Url " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        print(value_word)
        assert value_word == result
        print("Assertion Word GOOD")

    """Method Screenshot"""

    def get_screenshot(self, name):
        time.sleep(3)
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")  # Установка даты и времени
        name_screenshot = 'screenshot' + now_date + name + '.png'
        self.driver.save_screenshot('C:\\Users\\Алексей\\PycharmProjects\\dns_project\\screen\\' + name_screenshot)

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Assertion Url GOOD")

    """Method move to element"""

    def move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    """Method page down and home body"""

    def page_down_and_home_body(self):
        page = self.driver.find_element(By.TAG_NAME, "body")
        page.send_keys(Keys.PAGE_DOWN)
        page.send_keys(Keys.PAGE_DOWN)
        page.send_keys(Keys.PAGE_DOWN)
        page.send_keys(Keys.HOME)

    """Method history browser"""

    def back_history(self):
        self.driver.back()
        print("Back History")