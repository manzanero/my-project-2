import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dropdown")

select = driver.find_element(By.ID, "dropdown")
# select.click()
# select.send_keys(Keys.DOWN)
# select.send_keys(Keys.ENTER)

Select(select).select_by_visible_text("Option 1")

for i in range(len(Select(select).options)):
    print(Select(select).options[i].text)

time.sleep(3)