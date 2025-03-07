import os

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/upload")

file_upload = driver.find_element(By.ID, "file-upload")
file_upload.send_keys(os.getcwd() + "/puppy.png")

file_submit = driver.find_element(By.ID, "file-submit")
file_submit.click()
