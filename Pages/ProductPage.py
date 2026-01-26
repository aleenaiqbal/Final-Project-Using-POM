from selenium.webdriver.common.by import By
from Utils.SeleniumFunction import SeleniumFunction
from selenium.webdriver.support.ui import Select

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumFunction(driver)

        self.PRODUCT_TITLE = (By.XPATH, '//h3[text()="Create Your Own Cocktail"]')
        self.PRODUCT_PRICE = (By.XPATH, '//span[@class="price"]')
        self.PRODUCT_IMAGE = (By.XPATH, '//img[@class="product-image"]')
        self.STOCK = (By.XPATH, '//select[@name="storeId"]')
        self.QUANTITY = (By.XPATH, '//select[@class="product-quantity"]')
        self.ADD_TO_CART = (By.XPATH, '//button[text()="Add to cart"]')
        self.VIEW_CART = (By.XPATH, '//a[text()="View cart"]')

    def open_product(self):
        self.selenium.click(self.PRODUCT_TITLE)

    def get_title(self):
        return self.selenium.get_text(self.PRODUCT_TITLE)

    def get_price(self):
        return self.selenium.get_text(self.PRODUCT_PRICE)

    def select_stock(self, index):
        Select(self.driver.find_element(*self.STOCK)).select_by_index(index)

    def select_quantity(self, index):
        Select(self.driver.find_element(*self.QUANTITY)).select_by_index(index)

    def add_to_cart(self):
        self.selenium.click(self.ADD_TO_CART)

    def view_cart(self):
        self.selenium.click(self.VIEW_CART)





