import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/Users/laurentzerahmpakondema/Desktop/Drivers/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/register")

# example 1 locator matching with single element

# element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# element.send_keys("Apple Macbook Pro 13-inch")


# example 2: locator matching with multiple elements

# element = driver.find_element(By.XPATH, "//div[@class='footer-upper']//a")
# print(element.text)
# # example 3: element not available then throw no SuchElementException
# driver.find_element(By.CSS_SELECTOR, ".ico-login" ).click()

# example4: find elements... return multiple webElements
# elements = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
# print(len(elements))
# elements[0].send_keys("Apple Macbook Pro 13-inch")

elements = driver.find_elements(By.XPATH, "//div[@class='footer-upper']//a")
print(len(elements))
print(elements[1].text)

for ele in elements:
    print(ele.text)
