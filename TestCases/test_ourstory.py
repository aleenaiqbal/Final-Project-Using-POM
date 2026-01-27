import pytest
from Pages.OurStoryPage import OurStoryPage
from Config.conftest import setup

class TestOurStoryPage:
    def setup_method(self):
        self.base_url = 'https://ginandjuice.shop/about'

    @pytest.mark.story
    def test_our_story_page_load(self):
        page = OurStoryPage(self.driver)
        page.open_page()
        assert "about" in page.get_current_url()

    @pytest.mark.story
    def test_our_story_page_title(self):
        page = OurStoryPage(self.driver)
        page.open_page()
        assert "Our story - Gin & Juice Shop" in page.get_page_title()