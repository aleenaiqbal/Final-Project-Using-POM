import pytest
from Pages.LoginPage import LoginPage
import pytest_check as check
from Config.conftest import setup


class TestLogin:
    def  setup_method(self):
        self.base_url = 'https://ginandjuice.shop/login'

    @pytest.mark.login
    def test_login_valid(self):
        self.driver.get(self.base_url)
        login = LoginPage(self.driver)
        login.login("carlos", "hunter2")

    @pytest.mark.login
    def test_login_invalid_password(self):
        self.driver.get(self.base_url)
        login = LoginPage(self.driver)
        login.login("carlos", "abc")
        check.equal(login.get_error_message(),"Invalid username or password.")


