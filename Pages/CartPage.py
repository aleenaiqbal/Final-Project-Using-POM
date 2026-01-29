from operator import index
from selenium.webdriver.support.ui import Select


from selenium.webdriver.common.by import By
from Utils.SeleniumFunction import SeleniumFunction

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.selenium =SeleniumFunction(driver)

        self.ITEM_PRICE = (By.XPATH, '//span[@class="item-price"]')
        self.TOTAL_PRICE = (By.XPATH, '//strong')
        self.PLACE_ORDER = (By.XPATH, '//button[text()="Place order"]')
        self.CART_ITEMS = (By.XPATH, '//div[@class="cart-item"]')

        self.CART_ITEM_QUANTITY = (By.XPATH, './/select[@class="product-quantity"]')
        self.REMOVE_BUTTON = (By.XPATH, './/button[text()="Remove"]')
        self.ERROR_MSG = (By.XPATH,'//div[@class="empty-cart-icon"]')

    def get_item_price(self):
            return self.selenium.get_text(self.ITEM_PRICE)

    def get_total_price(self):
            return self.selenium.get_text(self.TOTAL_PRICE)

    def place_order(self):
            self.selenium.click(self.PLACE_ORDER)

    def get_item_count(self):
            return len(self.driver.find_elements(*self.CART_ITEMS))

    def remove_item(self, index):
            items = self.driver.find_elements(*self.CART_ITEMS)
            remove_btn = items[index].find_element(*self.REMOVE_BUTTON).click()
            remove_btn.click()

    def update_quantity(self, index, quantity):
        items = self.driver.find_elements(*self.CART_ITEMS)
        select_elem = Select(items[index].find_element(*self.CART_ITEM_QUANTITY))
        select_elem.select_by_index(quantity - 1)





