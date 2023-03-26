
### This class if for google home page and search for MyHeritage

class GoogleHomePage:
    def __init__(self, browser):
        self.browser = browser

    def write_in_search_bar_and_click_search(self, value):
        search = self.browser.find_element("name", "q")
        search.send_keys(value)
        search.submit()
