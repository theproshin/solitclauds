# encoding=utf-8
from hamcrest import assert_that, equal_to
from helpers.element import Element


__all__ = ['BasePage', ]


class BasePage(object):
    """Base page class for page object"""

    def __init__(self, driver):
        self.driver = driver
        self.__init_elements()

    def __init_elements(self):
        """set driver from element"""

        from helpers.element_list import ElementList

        for key, value in self.__class__.__dict__.items():
            if isinstance(value, (Element, ElementList)):
                value.driver = self.driver

    def open(self, url, title=None):
        """open url and check title
        :param url: page url
        :param title: title page for check
        """

        self.driver.get(url)
        if title:
            assert_that(self.driver.title, equal_to(title), 'Invalid title page')
