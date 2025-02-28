"""https://the-internet.herokuapp.com/nested_frames
find_element del elemento de en medio y que no falle"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/nested_frames")

driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-middle")

middle = driver.find_element(By.ID, "content")

driver.switch_to.default_content()