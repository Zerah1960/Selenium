from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/Users/laurentzerahmpakondema/Desktop/Drivers/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("ezadanger14@yahoo.com")
driver.find_element(By.ID, "pass").send_keys("foreveryoung5")
driver.find_element(By.NAME, "login']").click()