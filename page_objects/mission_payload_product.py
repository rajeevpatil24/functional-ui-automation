from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import product_urls, product_checks


class MissionPayload:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_link(self, xpath, description):
        """Generic method to click a link and handle errors."""
        try:
            link = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            link.click()
            print(f"{description} link clicked successfully")
        except Exception as e:
            print(f"Could not click {description}: {e}")

    def click_mission_payloads(self):
        """Click on the Mission Payloads product"""
        self.click_link("//a[@title='Mission Payloads']", "Mission Payloads")

    def load_product_page(self, url):
        """Navigate to a product page !"""
        self.driver.get(url)
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print(f"Loaded product page: {url}")

    def get_product_list(self):
        """Fetch product details (name, link, and read more text)."""
        product_data = []
        if not self.driver.find_elements(By.CLASS_NAME, 'shop_productlistdynamiccolumns'):
            print("No products found ")
            return product_data
        print("Product list found , getting details now !")
        for i in range(1, 3):
            prod_xpath = f"//div[@class='shop_productlistcolumn_item itemno{i}']"
            if i % 2 == 0:
                prod_xpath = f"//div[@class='shop_productlistcolumn_item itemno{i} alt']"
            product_items = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, prod_xpath)))
            for item in product_items:
                try:
                    product_name = item.find_element(By.XPATH, ".//strong[@class='name']/span").text
                    read_more_text = item.find_element(By.XPATH, ".//a[@class='viewproduct']/span").text
                    product_href = item.find_element(By.XPATH, ".//a[@class='viewproduct']").get_attribute("href")
                    product_data.append({
                        "product_name": product_name,
                        "read_more_text": read_more_text,
                        "href": product_href
                    })
                except NoSuchElementException:
                    print("No Element found to fetch details")
        return product_data

    def verify_product_page(self, url, expected_title):
        """Verify the title in product page """
        self.load_product_page(url)
        try:
            if self.driver.find_element(By.XPATH, f"//h1[contains(text(), '{expected_title}')]"):
                print(f" Successfully completed : {expected_title}")
        except NoSuchElementException:
            print(f"No Elelemtn Found : {expected_title}")

    def click_products(self):
        """Go to Product page , get product name from config file & verify the product details"""
        for url in product_urls:
            self.load_product_page(url)
        product_data = self.get_product_list()
        for product in product_data:
            name = product["product_name"]
            if name in product_checks:
                self.verify_product_page(product_checks[name], name)
            else:
                print("No products found , looks empty")
