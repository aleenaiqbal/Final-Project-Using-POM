import pytest

from Pages.HomePage import HomePage
from Config.conftest import setup

class TestHomePage:

    @pytest.mark.home
    def test_home_page_title(self):
        home = HomePage(self.driver)
        title = home.get_home_page_title()
        print("Home Page Title: ", title)
        assert "Home - Gin & Juice Shop" in title

    @pytest.mark.home
    def test_view_all_products(self):
        home = HomePage(self.driver)
        home.click_view_all_products()
        assert "/catalog" in self.driver.current_url

    @pytest.mark.home

    def test_click_first_product(self):
        home = HomePage(self.driver)
        home.click_first_product()
        assert "catalog/product" in self.driver.current_url

    @pytest.mark.home
    def test_view_post(self):
        home = HomePage(self.driver)
        home.click_view_post()
        assert "blog/post?postId=3" in self.driver.current_url

    @pytest.mark.home
    def test_subscribe_section(self):
        home = HomePage(self.driver)
        home.subscribe_newsletter("aleenaiqbal@ymail.com")

    @pytest.mark.home
    def test_web_vulnerability(self):
        home = HomePage(self.driver)
        home.click_web_vulnerability()
        assert "vulnerabilities" in self.driver.current_url

    @pytest.mark.home
    def test_view_all_product_link(self):
        home = HomePage(self.driver)
        home.click_view_all_product_link()
        assert "catalog" in self.driver.current_url

    @pytest.mark.home
    def test_view_all_blog_post(self):
        home = HomePage(self.driver)
        home.click_view_all_blog_post()
        assert "blog" in self.driver.current_url
