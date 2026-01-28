from selenium.webdriver.common.by import By
from Utils.SeleniumFunction import SeleniumFunction

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.selenium =SeleniumFunction(driver)

        self.USERNAME = (By.XPATH, '//input[@name="username"]')
        self.PASSWORD = (By.XPATH, '//input[@name="password"]')
        self.LOGIN_BTN = (By.XPATH, '//button[text()=" Log in "]')
        self.ERROR_MSG = (By.XPATH, '//p[@class="is-warning"]')

    def login(self, username, password):
        self.selenium.send_keys(self.USERNAME, username)
        self.selenium.click(self.LOGIN_BTN)
        self.selenium.send_keys(self.PASSWORD, password)
        self.selenium.click(self.LOGIN_BTN)

    def get_error_message(self,):
        return self.selenium.get_text(self.ERROR_MSG)