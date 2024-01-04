## Invisalign Providers Scraper
# Overview
This project aims to scrape data from the Invisalign Find a Doctor website, providing a list of dental treatment providers. The script is designed to collect essential details such as doctor names and locations.

# Features
Scraping Core Data:

Utilizes Selenium for automated web interactions.
Beautiful Soup is employed for HTML parsing to extract relevant information.

# Handling Cookies:

Manages the cookie acceptance popup to ensure uninterrupted scraping.

# Dynamic Search:

Allows dynamic searching by location to retrieve tailored results.

# Data Storage:

Stores scraped data in an Excel file for easy analysis.

# Requirements
Python (version 3.6 or higher)
Selenium (for web automation)
Beautiful Soup (for HTML parsing)
ChromeDriver (Chrome browser automation)

# Usage
Install the required Python packages:

```bash
pip install selenium beautifulsoup4 openpyxl 
```
Download and place the ChromeDriver executable in the project directory.

Run the script:

```bash
python find_doctors_scraper.py
```
The scraped data will be saved in an Excel file named doctors_data.xlsx.

Scaling the Scraper
To scale the scraper to multiple locations, modify the locations array in the script. The script is designed to iterate through each location, perform a search, and collect data.

locations = ['London', 'New York', 'Los Angeles', ...]

for location in locations:
    # ... (existing code)
    search_bar.send_keys(location)
    search_bar.send_keys(Keys.RETURN)
    # ... (existing code)

# Pagination Handling
The script currently handles pagination by implicitly waiting for elements to load after interacting with the search bar. If pagination is dynamic and requires explicit clicks, additional logic can be added within the script to navigate through pages.

# Example pagination handling
next_page_button = driver.find_element_by_class_name('next-page-button')

while next_page_button:
    next_page_button.click()
    # ... (existing code for scraping)
    next_page_button = driver.find_element_by_class_name('next-page-button')

# License
This project is licensed under the MIT License.

