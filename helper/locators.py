from selenium.webdriver.common.by import By

### This class locators is for the google locators - for example, find MyHeritage in google results page
class GoogleLocators:
    myhrittage_website = (By.XPATH, '//h3[.="MyHeritage"]')

#### This class locators is for MyHeritage website
class MyHeritageLocators:
    pricing_button = (By.ID, 'pricing')
    curreny_button = (By.CSS_SELECTOR, '.user_currency button')
    dollar_button = (By.XPATH, '//li[starts-with(.,"USD")]')
    prices_list_button = (By.CSS_SELECTOR, '.plan_price .list_price')
    plan_list_button = (By.CSS_SELECTOR, '.plan_name')