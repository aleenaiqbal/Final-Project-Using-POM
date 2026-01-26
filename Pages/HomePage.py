from selenium.webdriver.common.by import By
from Utils.SeleniumFunction import SeleniumFunction

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.selenium = SeleniumFunction(driver)


        self.view_all_products = (By.XPATH, '//a[@class="viewProductsButton"]')
        self.FIRST_PRODUCT = (By.XPATH, '//*[@id="productsPreview"]/div[2]/div[2]/section/a[1]/span[2]')
        self.VIEW_POST = (By.XPATH, '//a[text()="View post"]')
        self.SUBSCRIBE_INPUT = (By.XPATH, '//input[@name="email"]')
        self.SUBSCRIBE_BUTTON = (By.XPATH, '//button[@type="submit"]')
        self.WEB_VULNERABILITY = (By.XPATH, '//*[@id="productsPreview"]/div[1]/p/span')
        self.VIEW_ALL_PRODUCT_LINK = (By.XPATH, '//*[@id="productsPreview"]/a')
        self.VIEW_ALL_BLOG_POST = (By.XPATH, '//*[@id="blogPreview"]/a')

    def click_view_all_products(self):
        self.selenium.click(self.view_all_products)

    def get_home_page_title(self):
        return self.selenium.driver.title

    def click_first_product(self):
        self.selenium.click(self.FIRST_PRODUCT)

    def click_view_post(self):
        self.selenium.click(self.VIEW_POST)

    def subscribe_newsletter(self, email):
        self.selenium.send_keys(self.SUBSCRIBE_INPUT, email)
        self.selenium.click(self.SUBSCRIBE_BUTTON)

    def click_web_vulnerability(self):
        self.selenium.click(self.WEB_VULNERABILITY)

    def click_view_all_product_link(self):
        self.selenium.click(self.VIEW_ALL_PRODUCT_LINK)

    def click_view_all_blog_post(self):
        self.selenium.click(self.VIEW_ALL_BLOG_POST)




