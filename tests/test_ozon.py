import pytest
from pom.cart_page import CartPage
from pom.main_page import MainPage
import time

from pom.product_page import ProductPage
from pom.search_page import SearchPage


@pytest.mark.usefixtures('setup')
class TestOzon:

    def test_add_item_in_cart(self):
        main_page = MainPage(self.driver)
        main_page.fill_search_field_and_click("Mario")
        search_page = SearchPage(self.driver)
        itemname = search_page.find_item_in_search_result('text', 'Snickers Super')
        product_page = ProductPage(self.driver)
        product_page.add_item_in_cart(5)
        main_page.go_to_cart()
        cart_page = CartPage(self.driver)
        cart_page.check_if_item_in_cart_is_correct(itemname)
        cart_page.check_if_number_of_items_is_correct(5)
        time.sleep(3)




