import pytest
from Pages.BlogPage import BlogPage
import pytest_check as check
from Config.conftest import setup

@pytest.mark.blog
class TestBlogPage:
    def setup_method(self):
        self.base_url = 'https://ginandjuice.shop/blog'


    def test_blog_page_ui(self):
        blog = BlogPage(self.driver)
        blog.open_blog_page()

        #---------Soft Assertion----------

        check.is_in("blog", self.driver.current_url,"Blog URL is incorrect")
        check.is_in("Blog - Gin & Juice Shop", self.driver.title,"Blog page title is incorrect")
        check.is_true(blog.first_post_title_displayed(), "First blog post title is not visible")
        check.is_true(blog.first_post_image(), "First blog post image is not visible")
        check.is_true(blog.first_post_description(), "First blog post description is not visible")


    def test_search_blog(self):
        blog = BlogPage(self.driver)
        blog.open_blog_page()
        blog.search_blog("WHEEL")

    def test_view_blog_post(self):
        blog = BlogPage(self.driver)
        blog.open_blog_page()
        blog.view_blog()

