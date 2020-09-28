import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ch_options
from selenium.webdriver.firefox.options import Options as ff_options
from utils import json_config_parse

@pytest.fixture(scope='session')
def browser(): #def browser(browser_mode):

    #TODO: refactor this part
    browser_mode = json_config_parse.get_browser()

    # Initialize WebDriver
    if browser_mode == 'chrome':
        options = ch_options()
        # options.add_argument('--headless')
        options.add_argument('start-maximized')
        driver = webdriver.Chrome(executable_path='chromedriver', options=options)
    elif browser_mode == 'firefox':
        options = ff_options()
        options.add_argument('--headless')
        options.add_argument('start-maximized')
        driver = webdriver.Firefox(executable_path='geckodriver', options=options)
    else:
        raise Exception('browser is not a supported browser')

    driver.implicitly_wait('5')

    yield driver
    driver.quit()

# # START - parse from commandline options
# def pytest_addoption(parser):
#     parser.addoption(
#         '--browser',
#         action="store",
#         help='Choose you webdriver: chrome/firefox/safari',
#         required=False,
#         default='chrome'
#     )
#
#
# @pytest.fixture(scope='session')
# def browser_mode(pytestconfig):
#     driver_mode = pytestconfig.getoption("browser")
#     return driver_mode
# # END - parse from commandline options

