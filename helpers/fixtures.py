# encoding=utf-8
import pytest
from selenium import webdriver
from .config import Config


__all__ = ['browser', 'pytest']


@pytest.yield_fixture
def browser():
    """create instance browser"""

    config = Config()
    browser_name = config.get('general', 'browser')
    assert browser, 'Not found option "browser" in section "general"'
    browser_class = getattr(webdriver, browser_name, None)
    assert browser_class, 'Unknown browser {0}'.format(browser_class)
    driver = browser_class()
    driver.implicitly_wait(config.get('general', 'wait_time'))
    yield driver
    driver.quit()
