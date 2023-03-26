import os
import pytest

from helper.browser import Browser
from pages.google import GoogleHomePage
from pages.google_result_page import GoogleResultPage
from pages.myheritage_homePage import MyHeritageHomePage
from pages.pricing_list_page import PricingListPage


@pytest.fixture(scope="session")
def test_cases_setup():
    ### Create a new Browser instance and send Google website to browser - I could easilly remove the hardcoded google website and get it from the user
    browser = Browser()
    google_browser = browser.create_driver("http://www.google.com")

    #### create instance from Google homepage and search for MyHeritage
    google_home_page = GoogleHomePage(google_browser)
    google_home_page.write_in_search_bar_and_click_search("MyHeritage")

    #### create instance from Google page result and search for MyHeritage in google page result
    google_page_result = GoogleResultPage(google_browser)
    google_page_result.search_myheritage()

    ### create instance from my heritage home page and find the pricing button
    my_heritage_home_page = MyHeritageHomePage(google_browser)
    my_heritage_home_page.find_pricing()

    #### create instance from pricing page and get the list of the prices and the plans and remove the irrelavnt information
    pricing_list_page = PricingListPage(google_browser)
    pricing_list_page.search_for_change_currency_button()
    pricing_list_page.change_currency_to_dollar()
    prices_list = pricing_list_page.get_prices_list()
    plan_list = pricing_list_page.get_plan_list()

    ### create a new file called pricing_list.txt and write the pirces list to the file
    f = open("pricing_list.txt", "a")
    for plan, price in zip(plan_list, prices_list):
        if int(price) < 200:
            f.write(plan + " ")
            f.write(price)
            f.write('\n')
            print(plan, price)

    f.close()
    google_browser.quit()
