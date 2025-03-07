import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/horizontal_slider")


slider = driver.find_element(By.CSS_SELECTOR, "#content > div > div > input[type=range]")
slider.click()

for i in range(10):
    slider.send_keys(Keys.LEFT)

for i in range(6):
    slider.send_keys(Keys.RIGHT)

time.sleep(5)