from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import openpyxl
import time

chrome_options = ChromeOptions()
#chrome_options.add_argument('--disable-javascript')
driver = webdriver.Chrome()

# Open the Invisalign website
driver.get("https://www.invisalign.co.uk/find-a-doctor")

# Wait for the cookie popup to appear
cookie_popup = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'epdsubmit'))
)

# Click the accept button
ActionChains(driver).move_to_element(cookie_popup).click().perform()
time.sleep(5)
# Find the search bar input
search_bar = driver.find_element("name", "location")
search_bar.send_keys("London")

search_bar.send_keys(Keys.RETURN)



# Wait for the page to load (you might need to adjust the wait time)
driver.implicitly_wait(10)
time.sleep(10)

# Extract the HTML content after the search
html_content = driver.page_source
print(html_content)


# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Extract and print or store relevant information
results_container = soup.find('div', class_='dl-results-list')

# Create an Excel workbook and add a worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Set column headers
worksheet.append(['Doctor Name', 'Location'])

# Extract data for each doctor
for doctor_container in results_container.find_all('div', class_='dl-results-item-container'):
    name = doctor_container.find('div', class_='dl-item-container-inner').find('div', class_='item-cell-info').find('p', class_='dl-full-name').text.strip()
    location = doctor_container.find('div', class_='dl-item-container-inner').find('div', class_='item-cell-info').find_all('div')[1].text.strip()

    # Append data to the Excel worksheet
    worksheet.append([name, location])

# Save the Excel file
workbook.save('doctors_data.xlsx')

# Close the WebDriver
time.sleep(20)
driver.quit()
