from behave import *
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


@given('navego a "dynamic_content"')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://the-internet.herokuapp.com/dynamic_content")

@when('clico en "click here"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "click here").click()

@then('sale Mario')
def step_impl(context):
   try:
      avatar_mario = context.driver.find_element(
         By.CSS_SELECTOR, 'img[src="/img/avatars/Original-Facebook-Geek-Profile-Avatar-1.jpg"]')
   except NoSuchElementException as e:
      context.driver.save_screenshot("evidencia_error.png")
      raise AssertionError("Error no está Mario")