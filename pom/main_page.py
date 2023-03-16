import random

from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait




class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__search_field_l = "div input"
        self.__search_button_l = "button.x5-f"
        self.__go_to_cart_button_l = "//a[contains(@href,'cart')]"

    def fill_search_field_and_click(self, text):
        search_field = self.is_present("css", self.__search_field_l)
        search_field.send_keys(text)
        search_button = self.is_present("css", self.__search_button_l)
        search_button.click()
        # self.driver.find_element(By.CSS_SELECTOR, "div input").send_keys(text)
        # self.driver.find_element(By.CSS_SELECTOR, "button.x5-f").click()



    def add_item_in_cart(self):
        add_to_cart_button = WebDriverWait(self.driver, 5, 0.3).until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(),'корзину')]")))
        add_to_cart_button.click()
        add_to_cart_button.click()
        time.sleep(1)


    def go_to_cart(self):
        to_cart = self.is_present("xpath", self.__go_to_cart_button_l)
        to_cart.click()

    def check_if_item_is_in_cart(self, itemname):
        item_in_cart_name = WebDriverWait(self.driver, 5, 0.3).until(ec.presence_of_element_located((By.CSS_SELECTOR, "span.b6f span"))).text
        print(item_in_cart_name)
        assert itemname == item_in_cart_name

