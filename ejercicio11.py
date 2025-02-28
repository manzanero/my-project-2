"""https://the-internet.herokuapp.com/javascript_alerts
cilcar en el boton de confirmar y aceptar el alert
"""

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

boton = driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(1) > button")
boton.click()

alert = driver.switch_to.alert
alert.accept()

if driver.find_element(By.CSS_SELECTOR, "#result").text ==  "You successfully clicked an alert":
    print("Test passed")
else:
    print("Test failed")
