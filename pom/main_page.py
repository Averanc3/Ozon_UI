from selenium.webdriver.common.by import By
from .base_page import BasePage




class MainPage(BasePage):

    def fill_search_field(self, text):
        self.driver.find_element(By.CSS_SELECTOR, "div input").send_keys(text)
        self.driver.find_element(By.CSS_SELECTOR, "button.x5-f").click()