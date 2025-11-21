from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchPage(BasePage):
    # Locators
    FIRST_PRODUCT = (By.XPATH, "//div[@data-component-type='s-search-result'][1]//h2/a")
    PRODUCT_TITLE = (By.XPATH, "//div[@data-component-type='s-search-result'][1]//h2/a/span")
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result'][1]//span[@class='a-price-whole']")
    
    def get_first_product_name(self):
        return self.get_text(self.PRODUCT_TITLE)
    
    def get_first_product_price(self):
        try:
            return self.get_text(self.PRODUCT_PRICE)
        except:
            return "Price not available"
    
    def click_first_product(self):
        self.click_element(self.FIRST_PRODUCT)
