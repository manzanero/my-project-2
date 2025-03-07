import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/windows")

link = driver.find_element(By.LINK_TEXT, "Click Here")
link.click()

vieja_pestaña = driver.window_handles[0]
nueva_pestaña = driver.window_handles[1]

driver.switch_to.window(nueva_pestaña)

new = driver.find_element(By.CSS_SELECTOR, "body > div > h3")

driver.close()

driver.switch_to.window(vieja_pestaña)

link = driver.find_element(By.LINK_TEXT, "Click Here")

time.sleep(3)
