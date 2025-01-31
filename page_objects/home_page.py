from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self, url):
        """Open a webpage, accept cookies, and ensure full loading."""
        self.driver.get(url)
        self.driver.add_cookie({"name": "cookie_consent", "value": "true"})
        self.driver.refresh()
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print("Completed page Loading")

    def accept_cookies(self):
        """Allow all cookies button -> click if present."""
        try:
            cookie_button = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "ultimize_cookie_notification_allowallbutton"))
            )
            cookie_button.click()
            print("Cookies Accepted")
        except Exception as Exc:
            print(f"No cookie popup found. : {Exc}")



