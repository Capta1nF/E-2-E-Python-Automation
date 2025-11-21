import pytest
from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.driver_manager import DriverManager
from utils.excel_utils import ExcelUtils

class TestE2EAutomation:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = DriverManager.get_driver()
        self.driver.get("https://www.amazon.com")
        yield
        self.driver.quit()
    
    def test_search_and_add_to_cart(self):
        """E2E test: Search item, extract details, add to cart, capture screenshot, save to Excel"""
        
        # Initialize page objects
        home_page = HomePage(self.driver)
        search_page = SearchPage(self.driver)
        product_page = ProductPage(self.driver)
        cart_page = CartPage(self.driver)
        
        # Test data
        search_item = "iPhone 15"
        
        # Step 1: Search for item
        home_page.search_item(search_item)
        
        # Step 2: Get product details from search results
        product_name = search_page.get_first_product_name()
        product_price = search_page.get_first_product_price()
        
        # Step 3: Click on first product
        search_page.click_first_product()
        
        # Step 4: Extract detailed product information
        detailed_name = product_page.get_product_title()
        brand = product_page.get_brand()
        model = product_page.get_model()
        manufacturer = product_page.get_manufacturer()
        
        # Step 5: Add to cart
        product_page.add_to_cart()
        
        # Step 6: Verify item added to cart
        assert cart_page.is_item_added_to_cart(), "Item was not added to cart successfully"
        
        # Step 7: Take screenshot
        screenshot_path = cart_page.take_screenshot("item_added_to_cart")
        
        # Step 8: Prepare data for Excel
        test_data = {
            'Item_Name': detailed_name,
            'Model': model,
            'Manufacturer': manufacturer,
            'Brand': brand,
            'Price': product_price,
            'Test_Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'Screenshot_Path': screenshot_path,
            'Test_Status': 'PASSED'
        }
        
        # Step 9: Save to CSV
        csv_path = ExcelUtils.write_to_csv(test_data)
        print(f"Test data saved to: {csv_path}")
        print(f"Screenshot saved to: {screenshot_path}")
        
        # Assertions
        assert detailed_name, "Product name should not be empty"
        assert screenshot_path, "Screenshot should be captured"
        assert csv_path, "Data should be saved to CSV"
    
    def test_multiple_items_search(self):
        """Test searching for multiple items and saving results"""
        
        home_page = HomePage(self.driver)
        search_page = SearchPage(self.driver)
        
        search_items = ["MacBook Pro", "Samsung Galaxy", "Dell Laptop"]
        all_results = []
        
        for item in search_items:
            home_page.search_item(item)
            
            product_name = search_page.get_first_product_name()
            product_price = search_page.get_first_product_price()
            
            result_data = {
                'Search_Term': item,
                'Item_Name': product_name,
                'Price': product_price,
                'Test_Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'Test_Status': 'PASSED'
            }
            
            all_results.append(result_data)
            ExcelUtils.write_to_csv(result_data, "multiple_search_results.csv")
        
        # Create comprehensive report
        report_path = ExcelUtils.create_test_report(all_results)
        print(f"Comprehensive report saved to: {report_path}")
        
        assert len(all_results) == len(search_items), "All search items should be processed"
