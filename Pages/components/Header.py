from selenium.webdriver.common.by import By
from Utils.SeleniumFunction import SeleniumFunction

class Header:
    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumFunction(driver)

        self.PRODUCT_LINK = (By.XPATH , '//a[text()="Products"]')
        self.BLOG_LINK = (By.XPATH, '//a[text()="Blog"]')
        self.OUR_STORY_LINK = (By.XPATH, '//a[text()="Our story"]')

    def go_to_product(self):
        self.selenium.click(self.PRODUCT_LINK)

    def go_to_blog(self):
        self.selenium.click(self.BLOG_LINK)

    def go_to_our_story(self):
        self.selenium.click(self.OUR_STORY_LINK)



