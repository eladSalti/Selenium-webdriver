from selenium.webdriver.support import expected_conditions as ec
from helper.webdriversetup import WebDriverSetup
from helper.locators import GoogleLocators

### This class is for the results of the google search and find MyHeritage
class GoogleResultPage(WebDriverSetup):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = GoogleLocators

    def search_myheritage(self):
        myLink = self.wait_func().until(ec.element_to_be_clickable(self.locator.myhrittage_website))
        myLink.click()
