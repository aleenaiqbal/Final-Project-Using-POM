from selenium.webdriver.common.by import By
from Utils.SeleniumFunction import SeleniumFunction

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.selenium =SeleniumFunction(driver)

        self.ITEM_PRICE = (By.XPATH, '//span[@class="item-price"]')
        self.TOTAL_PRICE = (By.XPATH, '//strong')
        self.PLACE_ORDER = (By.XPATH, '//button[text()="Place order"]')

    def get_item_price(self):
            return self.selenium.get_text(self.ITEM_PRICE)

    def get_total_price(self):
            return self.selenium.get_text(self.TOTAL_PRICE)

    def place_order(self):
            self.selenium.click(self.PLACE_ORDER)


