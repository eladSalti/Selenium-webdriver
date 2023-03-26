from selenium.webdriver.support import expected_conditions as ec
from helper.webdriversetup import WebDriverSetup
from helper.locators import MyHeritageLocators

### This class is for MyHeritage homepage
class MyHeritageHomePage(WebDriverSetup):
    def __init__(self, browser):
        super().__init__(browser)
        self.locator = MyHeritageLocators

    def find_pricing(self):
        self.wait_func().until(ec.presence_of_element_located(self.locator.pricing_button)).click()
