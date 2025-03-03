import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class TestSelenium(unittest.TestCase):

    def test_esta_mario(self):
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/dynamic_content")
        try:
            avatar_mario = driver.find_element(
                By.CSS_SELECTOR,
                '#content > div:nth-child(1) > div.large-2.columns > img[sr"]')
        except NoSuchElementException as e:
            driver.save_screenshot("evidencia_error.png")
            raise AssertionError("Error no está Mario")


if __name__ == '__main__':
    unittest.main()