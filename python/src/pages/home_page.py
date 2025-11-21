from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    # Locators
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")
    
    def search_item(self, item_name):
        self.send_keys(self.SEARCH_BOX, item_name)
        self.click_element(self.SEARCH_BUTTON)
