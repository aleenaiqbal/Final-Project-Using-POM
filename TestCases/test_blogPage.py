import pytest
from Pages.BlogPage import BlogPage
from Config.conftest import setup

class TestBlogPage:
    def setup_method(self):
        self.base_url = 'https://ginandjuice.shop/blog'

    @pytest.mark.blog
    def test_blog_page_load(self):
        blog = BlogPage(self.driver)
        blog.open_blog_page()
        assert "blog" in self.driver.current_url

    @pytest.mark.blog
    def test_blog_page_title(self):
        blog = BlogPage(self.driver)
        blog.open_blog_page()
        assert "Blog - Gin & Juice Shop" in self.driver.title

    @pytest.mark.blog
    def test_blog_post_title_visible(self):
        blog = BlogPage(self.driver)
        blog.open_blog_page()
        assert blog.first_post_title_displayed()

    @pytest.mark.blog
    def test_blog_post_image_visible(self):
        blog = BlogPage(self.driver)
        blog.open_blog_page()
        assert blog.first_post_image()

    @pytest.mark.blog
    def test_blog_post_description_visible(self):
        blog = BlogPage(self.driver)
        blog.open_blog_page()
        assert blog.first_post_description()

    @pytest.mark.blog
    def test_search_blog(self):
        blog = BlogPage(self.driver)
        blog.open_blog_page()
        blog.search_blog("WHEEL")

    @pytest.mark.blog
    def test_view_blog_post(self):
        blog = BlogPage(self.driver)
        blog.open_blog_page()
        blog.view_blog()


