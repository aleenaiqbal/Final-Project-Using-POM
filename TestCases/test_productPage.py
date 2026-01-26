import pytest
from Pages.ProductPage import ProductPage
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