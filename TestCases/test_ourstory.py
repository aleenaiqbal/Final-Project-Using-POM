import pytest
from Pages.OurStoryPage import OurStoryPage
import pytest_check as check
from Config.conftest import setup

class TestOurStoryPage:

    @pytest.mark.story
    def test_our_story_page(self):
        page = OurStoryPage(self.driver)
        page.open_page()

        #--------Soft Assertion---------

        check.is_in("about",page.get_current_url(), "URL does not contain 'about'")
        check.is_in("Our story - Gin & Juice Shop", page.get_page_title(),
                    "Page title is incorrect")