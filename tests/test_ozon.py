import pytest
from pom.main_page import MainPage
import time



@pytest.mark.usefixtures('setup')
class TestOzon:
    def test_add_item_in_cart(self):
        url = "https://www.ozon.ru/"
        main_page = MainPage(self.driver, url)
        main_page.open()
        main_page.fill_search_field_and_click("Snickers")



