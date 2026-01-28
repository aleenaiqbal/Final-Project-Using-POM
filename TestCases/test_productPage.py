import pytest
from Pages.ProductPage import ProductPage
from Pages.CartPage import CartPage
from Config.conftest import setup

class TestProductPage:
    def  setup_method(self):
        self.base_url = 'https://ginandjuice.shop/catalog'

    @pytest.mark.product
    def test_product_page_title(self):
        self.driver.get(self.base_url)
        title = self.driver.title
        print("Product Page Title:", title)
        assert "Products - Gin & Juice Shop" in title

    @pytest.mark.product
    def test_page_load(self):
        self.driver.get(self.base_url)
        assert "catalog" in self.driver.current_url

    @pytest.mark.product
    def test_click_first_product(self):
        self.driver.get(self.base_url)
        product = ProductPage(self.driver)
        product.open_product()
        product.select_stock(1)
        product.select_quantity(5)
        product.add_to_cart()

    @pytest.mark.product
    def test_product_price_visible(self):
        self.driver.get(self.base_url)
        product = ProductPage(self.driver)
        assert product.is_product_price_visible()

    @pytest.mark.product
    def test_product_image_visible(self):
        self.driver.get(self.base_url)
        product = ProductPage(self.driver)
        assert product.is_product_image_visible()

    @pytest.mark.product
    def test_search_product(self):
        self.driver.get(self.base_url)
        product = ProductPage(self.driver)
        product.search_product("fruit")

    @pytest.mark.product
    def test_add_product_to_cart_single_quantity(self):
        self.driver.get(self.base_url)
        product = ProductPage(self.driver)
        product.open_product()
        product.select_stock(1)
        product.select_quantity(1)
        product.add_to_cart()

    @pytest.mark.product
    def test_add_multiple_products_to_cart(self):
        self.driver.get(self.base_url)
        product = ProductPage(self.driver)
        product.open_product()
        product.select_stock(1)
        product.select_quantity(2)
        product.add_to_cart()

        self.driver.get(self.base_url)
        product = ProductPage(self.driver)
        product.open_product()
        product.select_stock(1)
        product.select_quantity(3)
        product.add_to_cart()

