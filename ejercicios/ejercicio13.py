"""ir a https://the-internet.herokuapp.com/dynamic_controls
comprobar que hay un checkbok, pulsar en remove, comprobar que el check box desaparece
pulsar de nuevo en add, copromar que el checkbox aparece

luego pulsar el enable y escribir en el textbox "hola"

"""



import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

# boton_remove = driver.find_element(By.CSS_SELECTOR, "#checkbox-example > button")
# boton_add = driver.find_element(By.CSS_SELECTOR, "#checkbox-example > button")
#
#
# boton_remove.click()
#
# for i in range(10):
#     time.sleep(1)
#     try:
#         checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox > input[type=checkbox]")
#     except NoSuchElementException:
#         break
#
# try:
#     checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox > input[type=checkbox]")
#     raise AssertionError("sigue estando el checkbox")
# except NoSuchElementException:
#     pass
#
# boton_add.click()
#
# for i in range(10):
#     time.sleep(1)
#     try:
#         checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox")
#         break
#     except NoSuchElementException:
#         pass
#
# try:
#     checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox")
# except NoSuchElementException:
#     raise AssertionError("no esta el checkbox")


enable = driver.find_element(By.CSS_SELECTOR, "#input-example > button")
enable.click()

for i in range(10):
    time.sleep(1)
    try:
        textbox = driver.find_element(By.CSS_SELECTOR, "#input-example > input[type=text]")
        textbox.send_keys("hola")
        escribio = True
        break
    except ElementNotInteractableException:
        pass
else:
    raise AssertionError("no escribo")
