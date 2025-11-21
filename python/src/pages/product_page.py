from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    # Locators
    PRODUCT_TITLE = (By.ID, "productTitle")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    BRAND = (By.XPATH, "//tr[contains(.,'Brand')]//td[2]")
    MODEL = (By.XPATH, "//tr[contains(.,'Model')]//td[2]")
    MANUFACTURER = (By.XPATH, "//tr[contains(.,'Manufacturer')]//td[2]")
    
    def get_product_title(self):
        return self.get_text(self.PRODUCT_TITLE)
    
    def get_brand(self):
        try:
            return self.get_text(self.BRAND)
        except:
            return "Brand not available"
    
    def get_model(self):
        try:
            return self.get_text(self.MODEL)
        except:
            return "Model not available"
    
    def get_manufacturer(self):
        try:
            return self.get_text(self.MANUFACTURER)
        except:
            return "Manufacturer not available"
    
    def add_to_cart(self):
        self.click_element(self.ADD_TO_CART_BUTTON)
