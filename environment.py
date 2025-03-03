from selenium import webdriver


def before_all(context):
   pass

def before_feature(context, feature):
   pass

def before_scenario(context, scenario):
   context.driver = webdriver.Chrome()

def after_scenario(context, scenario):
   context.driver.quit()

def after_feature(context, feature):
   pass

def after_all(context):
   pass