"""en esta url https://the-internet.herokuapp.com/add_remove_elements/
click en el boton "Add Element" un numero aleatorio de veces entre 1 y 10
y luego hacer click en el boton "Delete" el mismo numero de veces que se hizo click en "Add Element"
comprobar que se eliminaron todos los elementos
"""
import time
from random import randint

from selenium import webdriver
from selenium.webdriver.common.by import By

veces = randint(1, 10)


class AddRemovePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.add_button = lambda: driver.find_element(By.CSS_SELECTOR, "#content > div > button")
        self.delete_buttons = lambda: driver.find_elements(By.CSS_SELECTOR, "#elements > button")

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

pagina = AddRemovePage(driver)


veces = 5

for i in range(veces):
    pagina.add_button().click()


total_botones = len(pagina.delete_buttons())

for i in range(total_botones):
    boton = pagina.delete_buttons()[- 1]
    boton.click()
    time.sleep(1)

time.sleep(5)
