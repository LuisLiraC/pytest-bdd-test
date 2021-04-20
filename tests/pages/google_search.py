from selenium.webdriver.common.by import By


class GoogleSearchPage:
    URL = 'https://www.google.com.mx/'
    SEARCH_INPUT = (By.NAME, 'q')

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def search(self, phrase):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)
        search_input.submit()
