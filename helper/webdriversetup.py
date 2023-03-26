from selenium.webdriver.support.wait import WebDriverWait

### This class is for WebDriver setup
class WebDriverSetup:
    def __init__(self, browser):
        self.browser = browser

### explicit wait function
    def wait_func(self):
        wait = WebDriverWait(self.browser, 10)
        return wait
