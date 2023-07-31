from selenium.webdriver.support import expected_conditions as EC
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

serv_obj = Service("/Users/laurentzerahmpakondema/Desktop/Drivers/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
mywait = WebDriverWait(driver,10)
driver.get("https://www.google.com/")
# driver.find_elements(By.XPATH, "//body[@class='EM1Mrb']").click()
driver.maximize_window()
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.submit()

search_link = mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))

search_link.click()


