import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/drag_and_drop")

a = driver.find_element(By.ID, "column-a")
b = driver.find_element(By.ID, "column-b")

ActionChains(driver).drag_and_drop(a, b).perform()
ActionChains(driver).drag_and_drop(b, a).perform()

time.sleep(5)