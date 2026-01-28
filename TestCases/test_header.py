import pytest
from Pages.components.Header import Header
import pytest_check as check
from Config.conftest import setup

class TestHeader:
    @pytest.mark.header
    def test_header_navigation(self):
        header = Header(self.driver)

        #-------Go To Product------------
        header.go_to_product()
        check.is_in("catalog",self.driver.current_url,"Product Page URL mismatch")

        #-------Go To Blog---------------
        header.go_to_blog()
        check.is_in("blog",self.driver.current_url,"Blog Page URL mismatch")

        #-------Go To Our Story----------
        header.go_to_our_story()
        check.is_in("about",self.driver.current_url,"Our Story Page URL mismatch")