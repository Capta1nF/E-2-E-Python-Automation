import pandas as pd
import os
from datetime import datetime

class ExcelUtils:
    @staticmethod
    def write_to_csv(data, filename="test_results.csv"):
        """Write test data to CSV file"""
        df = pd.DataFrame([data])
        
        # Create test-data directory if it doesn't exist
        os.makedirs("test-data", exist_ok=True)
        filepath = f"test-data/{filename}"
        
        # Check if file exists to determine if we need headers
        file_exists = os.path.exists(filepath)
        
        # Write to CSV
        df.to_csv(filepath, mode='a', header=not file_exists, index=False)
        return filepath
    
    @staticmethod
    def create_test_report(test_results, filename=None):
        """Create detailed test report in Excel format"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"test_report_{timestamp}.xlsx"
        
        os.makedirs("reports", exist_ok=True)
        filepath = f"reports/{filename}"
        
        df = pd.DataFrame(test_results)
        df.to_excel(filepath, index=False)
        return filepath
