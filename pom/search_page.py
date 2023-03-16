import random
import time


from pom.base_page import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__found_items_l = '//a[contains(@href,"product")]/span/span'


    def find_item_in_search_result(self, search_type, search_what):
        time.sleep(2)
        if search_type == 'text':

            results = self.are_present('xpath', "//a[contains(@href,'product')]/span/span")
            # for result in results:
            #     print(result.text)
            #     if search_what in result.text:
            #         result.click()

            print("WHOA!", len(results))

            res = results[random.randint(1,len(results))]
            print(res.text)
            itemname = res.text
            res.click()
            return itemname
        elif search_type == 'price':
            pass