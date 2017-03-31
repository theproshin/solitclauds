# encoding=utf-8
from helpers.element import Element
from hamcrest import assert_that, greater_than_or_equal_to
from selenium.webdriver.support.wait import WebDriverWait
from .config import Config


__all__ = ['ElementList']


class ElementItem(Element):

    def __init__(self, webelement=None, by=None, value=None, name=None):
        super().__init__(by, value, name)
        self.webelement = webelement

    def get_webelement(self):
        return self.webelement


class ElementList(object):

    def __init__(self, by, value, name):
        self.by = by
        self.value = value
        self.name = name
        self.driver = None

    def __getitem__(self, index):
        return self.find_by_index(index)

    def get_webelements(self):
        """get list instance ElementItem"""

        wait_time = Config().get('general', 'wait_time')
        wait_time = int(wait_time) if wait_time else 0
        return WebDriverWait(self.driver, wait_time).until(
            lambda driver: driver.find_elements(self.by, self.value),
        )

    def find_by_index(self, index):
        """find element by index
        :param index: index element
        """

        webelements = self.get_webelements()
        assert_that(len(webelements), greater_than_or_equal_to(index),
                    'Element by number {0} not found'.format(index))
        return ElementItem(webelements[index])
