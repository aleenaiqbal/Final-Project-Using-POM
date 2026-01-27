from selenium.webdriver.common.by import By
from Utils.SeleniumFunction import SeleniumFunction

class OurStoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.selenium =SeleniumFunction(driver)
        self.url = 'https://ginandjuice.shop/about'

    def open_page(self):
        self.driver.get(self.url)

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url