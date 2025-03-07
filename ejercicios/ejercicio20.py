import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/jqueryui/menu")

enabled = driver.find_element(By.CSS_SELECTOR, "#ui-id-3 > a")
downloads = driver.find_element(By.CSS_SELECTOR, "#ui-id-4 > a")
pdf = driver.find_element(By.CSS_SELECTOR, "#ui-id-5 > a")

hover1 = ActionChains(driver).move_to_element(enabled)
hover1.perform()
time.sleep(1)
hover2 = ActionChains(driver).move_to_element(downloads)
hover2.perform()
time.sleep(1)
pdf.click()

time.sleep(5)