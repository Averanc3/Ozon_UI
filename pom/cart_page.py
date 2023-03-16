from pom.base_page import BasePage
import re


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__item_in_cart_name_l = "a.tsBodyM span span"
        self.__number_of_items_l = "//span[contains(text(),'товаров')]"



    def check_items_number(self):
        pass


    def check_if_item_in_cart_is_correct(self, itemname: str):
        item_in_cart_name = self.is_present("css", self.__item_in_cart_name_l).text
        assert itemname == item_in_cart_name, 'Name of the item in cart isn\'t equal to the one added'

    def check_if_number_of_items_is_correct(self, number_of_items: int):
        actual_number_of_items_text = self.is_present("xpath", self.__number_of_items_l).text
        actual_number_of_items = int(re.findall("\d+", actual_number_of_items_text)[0])
        assert number_of_items == actual_number_of_items, f"You're getting number of items={actual_number_of_items} " \
                                                          f"different from what you ordered={number_of_items}"

