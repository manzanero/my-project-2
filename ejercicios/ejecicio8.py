"""crear metodo que reciba dos parametros booleanos y
que deje el estado final igual en la página
https://the-internet.herokuapp.com/checkboxes"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class CheckboxesPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.checkbox1 = lambda: driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(1)")
        self.checkbox2 = lambda: driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(3)")

    def dame_checkbox(self, n):
        return driver.find_element(By.CSS_SELECTOR, f"#checkboxes > input[type=checkbox]:nth-child({n})")

    def esta_checkbox1_seleccionada(self):
        try:
            driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox][checked]:nth-child(1)")
            return True
        except:
            return False

    def esta_checkbox2_seleccionada(self):
        try:
            driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox][checked]:nth-child(3)")
            return True
        except:
            return False


driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/checkboxes")

pagina = CheckboxesPage(driver)


def marcar_checkboxes(chk1, chk2):
    if chk1 and not pagina.dame_checkbox(1).is_selected():
        pagina.checkbox1().click()
    if not chk1 and pagina.dame_checkbox(1).is_selected():
        pagina.checkbox1().click()

    if chk2 and not pagina.dame_checkbox(3).is_selected():
        pagina.checkbox2().click()
    if not chk2 and pagina.dame_checkbox(3).is_selected():
        pagina.checkbox2().click()


marcar_checkboxes(True, False)

time.sleep(5)