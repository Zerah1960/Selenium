from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/Users/laurentzerahmpakondema/Desktop/Drivers/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://automationpractice.com/index.php")
driver.maximize_window()

"""
CSS selector
tagname are not obliged
tag id: tagname#valueId  input#email
tag class tagname.valueofclass  input.inputtext _55r1 _6luy
tag attribute tagname[attribut=value] input[data-testid=royal_email]
tag class attribute tagname.valueofClass[attribute=value] 
                                    input.inputtext[]

"""