from selenium.webdriver.common.by import By
from Utils.SeleniumFunction import SeleniumFunction

class BlogPage:
    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumFunction(driver)
        self.url = "https://ginandjuice.shop/blog/"

        # Locators
        self.FIRST_POST_TITLE = (By.XPATH, '//h2[text()="A Hairy Day"]')
        self.FIRST_POST_IMAGE = (By.XPATH, '/html/body/div[2]/section/div/section[2]/div[1]/a[1]/img')
        self.FIRST_POST_DESCRIPTION = (By.XPATH, '/html/body/div[2]/section/div/section[2]/div[1]/p')
        self.SEARCH_INPUT = (By.XPATH, '//input[@type="text"]')
        self.SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
        self.VIEW_POST_BUTTON = (By.XPATH, '//a[@class="button is-small"]')

    def open_blog_page(self):
        self.driver.get(self.url)

    def first_post_title_displayed(self):
        return self.selenium.is_displayed(self.FIRST_POST_TITLE)

    def first_post_image(self):
        return self.selenium.is_displayed(self.FIRST_POST_IMAGE)

    def first_post_description(self):
        return self.selenium.is_displayed(self.FIRST_POST_DESCRIPTION)

    def search_blog(self, text):
        self.selenium.send_keys(self.SEARCH_INPUT, text)
        self.selenium.click(self.SEARCH_BUTTON)

    def view_blog(self):
        self.selenium.click(self.VIEW_POST_BUTTON)
