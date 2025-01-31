from time import sleep

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def chrome_browser():
    driver = webdriver.Chrome()  # Initialize Chrome browser
    driver.set_window_size(1920, 1080)  # Full HD resolution
    yield driver  # Provide WebDriver instance to the test
    sleep(10)
    #driver.quit()  # Cleanup after test execution


