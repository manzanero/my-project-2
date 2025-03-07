import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

prefs = {
    "download.default_directory": "C:/Users/alejandro.manzanero/workspaces/my-project-2/downloads",
    "download.directory_upgrade": True,
    "download.prompt_for_download": False,
}

options = Options()
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/download")

link = driver.find_element(By.LINK_TEXT, "puppy.png")
link.click()

time.sleep(50)