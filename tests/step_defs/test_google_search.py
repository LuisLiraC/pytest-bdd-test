from pytest_bdd import scenarios, when, then, given
from tests.pages.google_search import GoogleSearchPage
from tests.pages.google_results import GoogleResultsPage


CONVERTERS = {
    'amount': int
}

scenarios('../features/google_search.feature', example_converters=CONVERTERS)


@given('the Google Home Page is displayed', target_fixture='browser')
def google_home(browser):
    b = GoogleSearchPage(browser)
    b.load()
    return b


@when('the user searches for "<phrase>"')
def search_phrase(browser: GoogleSearchPage, phrase):
    browser.search(phrase)


@then('results are shown for "<phrase>"')
def search_result(browser: GoogleSearchPage, phrase):
    results_page = GoogleResultsPage(browser.driver)
    assert results_page.search_input_value() == phrase


@then('print "<amount>" results')
def print_results(browser: GoogleSearchPage, amount):
    results_page = GoogleResultsPage(browser.driver)
    results_titles = results_page.result_link_titles()
    assert len(results_titles) > 0
    results_page.print_results(amount, results_titles)




