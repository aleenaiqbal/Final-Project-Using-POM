from selenium.webdriver.common.by import By
from Utils.SeleniumFunction import SeleniumFunction

class Footer:
    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumFunction(driver)

        self.PRODUCT_LINK = (By.XPATH,'/html/body/div[2]/div/section[2]/div/nav/ul/li[1]/a')
        self.BLOG_LINK = (By.XPATH,'/html/body/div[2]/div/section[2]/div/nav/ul/li[2]/a')
        self.OURSTORY_LINK = (By.XPATH,'/html/body/div[2]/div/section[2]/div/nav/ul/li[3]/a')


    def go_to_product(self):
        self.selenium.click(self.PRODUCT_LINK)

    def go_to_blog(self):
        self.selenium.click(self.BLOG_LINK)

    def go_to_our_story(self):
        self.selenium.click(self.OURSTORY_LINK)

