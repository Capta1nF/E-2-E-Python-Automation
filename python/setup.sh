#!/bin/bash

echo "Setting up Python E2E Automation Framework..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p screenshots reports test-data

echo "Setup complete!"
echo ""
echo "To activate virtual environment: source venv/bin/activate"
echo "To run tests: pytest"
echo "To generate Allure report: pytest --alluredir=reports/allure-results && allure serve reports/allure-results"
