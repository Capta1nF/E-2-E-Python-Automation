# Python E2E Automation Framework

Complete automation framework using Selenium WebDriver, Pytest, and Page Object Model.

## Features
- ✅ Page Object Model (POM) architecture
- ✅ E2E test automation (Search → Add to Cart → Screenshot → Excel)
- ✅ Screenshot capture functionality
- ✅ Excel/CSV data export
- ✅ Pytest HTML & Allure reporting
- ✅ Cross-browser support

## Setup

1. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

2. **Install Allure (for reporting):**
```bash
# macOS
brew install allure

# Or download from: https://docs.qameta.io/allure/
```

## Running Tests

### Basic Test Execution
```bash
# Run all tests
pytest

# Run specific test
pytest src/tests/test_e2e_automation.py::TestE2EAutomation::test_search_and_add_to_cart

# Run with HTML report
pytest --html=reports/report.html --self-contained-html
```

### Generate Allure Reports
```bash
# Run tests with Allure
pytest --alluredir=reports/allure-results

# Generate and serve Allure report
allure serve reports/allure-results
```

## Project Structure
```
python/
├── src/
│   ├── pages/          # Page Object classes
│   ├── tests/          # Test cases
│   └── utils/          # Utility classes
├── screenshots/        # Test screenshots
├── reports/           # Test reports
├── test-data/         # Excel/CSV files
└── requirements.txt   # Dependencies
```

## Test Results
- **Screenshots**: Saved in `screenshots/` folder
- **Excel Data**: Saved in `test-data/` folder
- **Reports**: HTML and Allure reports in `reports/` folder

## Key Test Cases
1. **test_search_and_add_to_cart**: Complete E2E workflow
2. **test_multiple_items_search**: Batch search testing
