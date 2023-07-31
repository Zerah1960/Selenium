from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/Users/laurentzerahmpakondema/Desktop/Drivers/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://automationpractice.com/index.php")
driver.maximize_window()
"""
XPATH
//tagname[@attribute="value"]
//tagname[contains(@attribute,"value")]      //input[contains(@id,"search")]
//tagname[starts-with(@attribute,"value")]       //button[starts-with(@name,"submit_")]
//a[text()="Women"]
"""