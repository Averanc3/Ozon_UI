import time

from selenium.webdriver.common.by import By

from pom.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__add_to_cart_button_l = "//span[contains(text(),'корзину')]"
        self.__add_more_items_l = "//span[text()= '1']/following-sibling::div/button"
        self.__out_of_stock = "//div[contains(text(), 'В наличии больше нет')]"


    def add_item_in_cart(self, number_of_items = 1):
        add_to_cart_button = self.is_present('xpath', self.__add_to_cart_button_l)
        add_to_cart_button.click()
        add_to_cart_button.click()
        if number_of_items > 1:
            add_more = self.is_present('xpath', self.__add_more_items_l)
            for item in range(number_of_items-1):
                add_more.click()

        time.sleep(1)

