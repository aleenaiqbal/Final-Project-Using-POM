from itertools import product

import pytest

from Pages.CartPage import CartPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.ProductPage import ProductPage
from Pages.CartPage import CartPage
from Pages.LoginPage import LoginPage
from Config.conftest import setup
import pytest_check as check



class TestFlow:
    @pytest.mark.flow
    def test_complete_flow(self):
        home = HomePage(self.driver)
        home.click_view_all_products()
        assert "catalog" in self.driver.current_url

        product = ProductPage(self.driver)

        product.open_product()
        assert product.get_title().lower() == "Create Your Own Cocktail".lower()
        assert product.get_price() == "$84.96"

        product.select_stock(1)
        product.select_quantity(5)
        product.add_to_cart()
        product.view_cart()

        cart = CartPage(self.driver)

        self.item_price = float(cart.get_item_price().replace("$", ""))
        expected_total = round(self.item_price * 6, 2)

        total_price = float(cart.get_total_price().replace("$", ""))
        assert expected_total == total_price

        cart.place_order()

        login =LoginPage(self.driver)
        login.login("carlos", "hunter2")

    @pytest.mark.regression
    def test_cart_total_updates_when_quantity_changes(self):
        """
        Verify cart total updates correctly when quantity changes
        """

        home = HomePage(self.driver)
        home.click_view_all_products()

        product = ProductPage(self.driver)
        product.open_product()

        product.select_stock(1)
        product.select_quantity(2)
        product.add_to_cart()
        product.view_cart()

        cart = CartPage(self.driver)
        item_price = float(cart.get_item_price().replace("$", ""))

        total_price = float(cart.get_total_price().replace("$", ""))
        expected_total = round(item_price * 3, 2)

        assert total_price == expected_total
