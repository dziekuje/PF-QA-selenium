import pytest

from selenium.webdriver.common.keys import Keys
from utils import json_config_parse


MAINURL = json_config_parse.get_mainurl()


def test_duckduckgo_title(browser):
    endpoint = (MAINURL+'/')
    browser.get(endpoint)
    assert browser.title == 'DuckDuckGo — Privacy, simplified.'


def test_duckduckgo_logo_text(browser):
    endpoint = (MAINURL+'/')
    browser.get(endpoint)
    assert browser.find_element_by_css_selector("#logo_homepage_link").text == 'About DuckDuckGo'


def test_duckduckgo_search(browser):
    endpoint = (MAINURL+'/')
    browser.get(endpoint)
    search_phrase = "looking for something"
    # find search bar
    search_bar = browser.find_element_by_css_selector("#search_form_input_homepage")
    # enter "looking for something" in search field
    search_bar.send_keys(search_phrase + Keys.ENTER)
    # check if our search phrase is equal to the phrase on result page
    search_result = browser.find_element_by_css_selector("#search_form_input").get_attribute("value")
    assert search_result == search_phrase