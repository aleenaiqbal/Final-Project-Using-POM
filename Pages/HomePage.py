from selenium.webdriver.common.by import By
from Utils.SeleniumFunction import SeleniumFunction

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumFunction(driver)


        self.view_all_products = (By.XPATH, '//a[@class="viewProductsButton"]')

    def click_view_all_products(self):
        self.selenium.click(self.view_all_products)


