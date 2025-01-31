# UI  Test Automation Project

## Overview

This project is a  UI test automation suite using **`pytest`** and **`Selenium`**,
designed to validate the functionality of a web application. 
It includes test cases for interacting with web elements, handling cookies, navigating through product pages & verifying the flow.

### Features:
- **HomePage Tests**: Dashboard Page with accepting cookies
- **Mission Payloads Tests**: Verifies product details are displayed properly.


## Prerequisites

Before running the tests, make sure you have the following installed:

- Python 3
- Selenium
- Pytest
- Pytest-html (for custom HTML reports)

To install dependencies Run below command in terminal:

pip install -r requirements.txt


## Running Tests

To run the tests, use the following command:

pytest tests/test_home.py -s -v --html=report.html
pytest tests/test_mission_payload_product.py -s -v --html=report.html
