import pytest
from page_objects.home_page import HomePage
from config.config import url
from utils.screenshot_utils import capture_screenshot


@pytest.mark.home
def test_home_page(chrome_browser):
    '''
    Test launch of Home Page
    '''
    home_page = HomePage(chrome_browser)
    home_page.open_page(url)
    home_page.accept_cookies()
    capture_screenshot(chrome_browser, "test_home_page")
    #home_page.click_products()
