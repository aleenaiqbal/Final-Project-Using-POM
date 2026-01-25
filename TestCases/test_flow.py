from itertools import product

import pytest
from Pages.HomePage import HomePage
from Pages.ProductPage import ProductPage
from Config.conftest import setup



class TestFlow:
    def test_complete_flow(self):
        home = HomePage(self.driver)
        home.click_view_all_products()
        assert "catalog" in self.driver.current_url

        product = ProductPage(self.driver)

        product.open_product()
        assert product.get_title().lower() == "Create Your Own Cocktail".lower()
        assert product.get_price() == "$84.96"
