from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/laurentzerahmpakondema/Desktop/Drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj)
"""
First we need to import webdriver from selenium and then from the
Chrome class we have to create object called driver and all the methods
will be available.

create object for a class
"""

driver = webdriver.Chrome("/Users/laurentzerahmpakondema/Desktop/Drivers/chromedriver")
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()

print("Test completed !!!")

