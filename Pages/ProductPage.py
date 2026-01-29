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

        self.VIEW_DETAILS = (By.XPATH, '//span[text()="View details"]')
        self.CHECK_STOCK = (By.XPATH, '//button[text()="Check stock"]')

        #self.PRODUCT_PRICE = (By.XPATH, '//span[text()="$30.50"]')
        #self.PRODUCT_IMAGE = (By.XPATH, '/html/body/div[2]/section/div/section[3]/a[1]/img[1]')

        self.SEARCH_INPUT = (By.XPATH, '//input[@id="searchBar"]')
        self.SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')

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

    def is_product_price_visible(self):
        return self.selenium.is_displayed(self.PRODUCT_PRICE)

    def is_product_image_visible(self):
        return self.selenium.is_displayed(self.PRODUCT_IMAGE)

    def search_product(self, text):
        self.selenium.send_keys(self.SEARCH_INPUT, text)
        self.selenium.click(self.SEARCH_BUTTON)





