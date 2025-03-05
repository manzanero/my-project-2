"""https://the-internet.herokuapp.com/hovers clicar en el enlace
que sale al poner el ratón por encima de la imagen
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/hovers")

avatar = driver.find_element(By.CSS_SELECTOR, "#content > div > div:nth-child(3) > img")

hover = ActionChains(driver).move_to_element(avatar)
hover.perform()


link = driver.find_element(By.CSS_SELECTOR, "#content > div > div:nth-child(3) > div > a")

link.click()

time.sleep(5)