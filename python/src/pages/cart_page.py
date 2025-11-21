from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    # Locators
    CART_ITEM = (By.XPATH, "//div[@id='sw-atc-details-single-container']")
    CART_SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'a-alert-success')]")
    GO_TO_CART = (By.ID, "sw-atc-goto-cart-button")
    
    def is_item_added_to_cart(self):
        try:
            return self.find_element(self.CART_SUCCESS_MESSAGE).is_displayed()
        except:
            return False
    
    def go_to_cart(self):
        self.click_element(self.GO_TO_CART)
