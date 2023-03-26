from selenium.webdriver.support import expected_conditions as ec
from helper.webdriversetup import WebDriverSetup
from helper.locators import MyHeritageLocators

### This class is for pricing page in MyHeritage
class PricingListPage(WebDriverSetup):
    def __init__(self,browser):
        super().__init__(browser)
        self.locator = MyHeritageLocators

#### This func is to click on change currency
    def search_for_change_currency_button(self):
        self.wait_func().until(ec.element_to_be_clickable(self.locator.curreny_button)).click()

### This func is to change current currency to Dollar - I could easilly remove the hardcoded dollar and get the cuerrency from the user
    def change_currency_to_dollar(self):
        self.wait_func().until(ec.element_to_be_clickable(self.locator.dollar_button)).click()

#### Get prices list and split the prices from the irrelevant information
    def get_prices_list(self):
        prices_list = self.wait_func().until(
            ec.visibility_of_all_elements_located(self.locator.prices_list_button))
        prices_list_final = [price.text.split("/")[0][1:] for price in prices_list]
        return prices_list_final

### Get the plan list
    def get_plan_list(self):
        plan_list = self.wait_func().until(ec.visibility_of_all_elements_located(self.locator.plan_list_button))
        plan_list_final = [price.text for price in plan_list[1:]]
        return plan_list_final
