import pytest
from Pages.components.Footer import Footer
import pytest_check as check
from Config.conftest import setup

class TestFooter:
    @pytest.mark.footer
    def test_footer_navigation(self):
        footer = Footer(self.driver)

        footer.go_to_product()
        check.is_in("catalog",self.driver.current_url,"Product Page URL mismatch")

        footer.go_to_blog()
        check.is_in("blog",self.driver.current_url,"Blog Page URL mismatch")

        footer.go_to_our_story()
        check.is_in("about",self.driver.current_url,"Our Story Page URL mismatch")

