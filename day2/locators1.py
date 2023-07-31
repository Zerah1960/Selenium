from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/Users/laurentzerahmpakondema/Desktop/Drivers/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com")
driver.maximize_window()
# driver.find_element(By.NAME, "q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element(By.CSS_SELECTOR, ".button-1.search-box-button").click()
driver.find_element(By.LINK_TEXT, "Register").click()