from selenium import webdriver

#### This class is to create a new webdriver of Firefox
class Browser:
    def create_driver(self,url):
        # Create a new webdriver object
        browser = webdriver.Firefox()
        # open in full screen
        browser.maximize_window()
        # launches a new browser with google.com domain
        browser.get(url)

        return browser

