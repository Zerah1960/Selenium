from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/Users/laurentzerahmpakondema/Desktop/Drivers/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()
search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print(search_box.is_displayed())
print(search_box.is_enabled())

rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female = driver.find_element(By.CSS_SELECTOR, "#gender-female")
print(rd_male.is_selected())
print(rd_female.is_selected())
rd_male.click()
print("After selecting male radio button....")
print(rd_male.is_selected())
print(rd_female.is_selected())

rd_female.click()
print("After selecting female radio button")
print(rd_male.is_selected())
print(rd_female.is_selected())



# is_displayed()    is_displayed