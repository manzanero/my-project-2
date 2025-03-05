from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/tables")

def get(fila, columna):
    celda = driver.find_element(By.CSS_SELECTOR, f"#table1 > tbody > tr:nth-child({fila}) > td:nth-child({columna})")
    return celda

i = 0
try:
    while True:
        i = i + 1
        celda = get(i, 4)
        due = celda.text
        due = due.lstrip('$')
        due = float(due)
        if due > 50:
            continue

        print(get(i, 1).text + " " + get(i, 2).text)
except NoSuchElementException:
    pass