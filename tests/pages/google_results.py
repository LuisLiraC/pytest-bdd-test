from selenium.webdriver.common.by import By


class GoogleResultsPage:
    RESULT_LINKS_TITLES = (By.CSS_SELECTOR, '#rso div.yuRUbf > a > h3')
    SEARCH_INPUT = (By.NAME, 'q')

    def __init__(self, driver):
        self.driver = driver

    def result_link_titles(self):
        links = self.driver.find_elements(*self.RESULT_LINKS_TITLES)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.driver.title

    def print_results(self, amount, results):
        if amount < len(results):
            n = amount
        else:
            n = len(results)

        for i in range(n):
            print(results[i])
