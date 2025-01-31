import pytest

from page_objects.home_page import HomePage
from page_objects.mission_payload_product import MissionPayload
from config.config import url
from utils.screenshot_utils import capture_screenshot


@pytest.mark.payload
def test_payload_mission(chrome_browser):
    '''
    Test launch of Home Page
    '''
    home_page = HomePage(chrome_browser)
    home_page.open_page(url)
    home_page.accept_cookies()
    capture_screenshot(chrome_browser, "test_home_page")
    mission_payload_page = MissionPayload(chrome_browser)
    mission_payload_page.click_mission_payloads()
    capture_screenshot(chrome_browser, "test_product_page")
    mission_payload_page.click_products()
    capture_screenshot(chrome_browser, "test_product_page")