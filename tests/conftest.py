import os
import sys
import pytest
import json
from selenium import webdriver


sys.path.append(os.path.dirname(sys.path[0]))
BROWSERS = ['Firefox', 'Chrome', 'Edge', 'Headless Chrome']


@pytest.fixture
def config(scope='session'):
    with open('config.json') as config_file:
        config = json.load(config_file)

    assert config['browser'] in BROWSERS
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    return config


@pytest.fixture
def browser(config):
    b = config['browser']

    if b == 'Chrome':
        driver = webdriver.Chrome()
    elif b == 'Firefox':
        driver = webdriver.Firefox()
    elif b == 'Edge':
        driver = webdriver.Edge()
    elif b == 'Headless Chrome':
        opts = webdriver.ChromeOptions()
        opts.add_argument('headless')
        driver = webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{b}" is not supported')

    driver.implicitly_wait(config['implicit_wait'])
    yield driver
    driver.quit()
