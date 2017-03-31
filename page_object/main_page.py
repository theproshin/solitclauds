from helpers.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from hamcrest import assert_that, equal_to, is_in
from helpers.element import Element, Input
from helpers.element_list import ElementList
import allure


class MainPage(BasePage):

    search_elm = Input(By.CSS_SELECTOR, '#gs_lc0>input', 'search')
    search_results = ElementList(By.CSS_SELECTOR, '.srg>.g a', 'first link')
    tabs = ElementList(By.CSS_SELECTOR, '#hdtb-msb-vis a', 'image tab')
    current_tab = Element(By.CSS_SELECTOR, '#hdtb-msb-vis>.hdtb-msel', 'current tab')
    images = ElementList(By.CSS_SELECTOR, '[data-ri="0"] a', 'first image')

    def search(self, text, clear=True):
        """search by text
        :param text: search text
        :param clear: clear input or not
        """

        with allure.step('search text "{0}"'.format(text)):
            if clear:
                self.search_elm.clear()
            self.search_elm.send_keys(text + Keys.ENTER)
            assert_that(self.search_elm.text, equal_to(text), 'Wrong text in search')

    def check_result_url(self, number, url, contains=True):
        """check url in result search
        :param number: number of result search
        :param url: url
        :param contains: exact or contains text
        """

        with allure.step('check result number "{0}" have url {1}'.format(number, url)):
            matcher = is_in if contains else equal_to
            href = self.search_results[number].get_attribute('href')
            assert_that(url, matcher(href), 'Wrong url from first link')
            return href

    def select_tab_by_text(self, text):
        """select tab by text
        :param text: tab text
        """
        with allure.step('select tab "{0}"'.format(text)):
            tabs = ['Все', 'Картинки', 'Видео', 'Новости', 'Покупки', 'Еще', 'Настройки', 'Инструменты']
            tabs.remove(self.current_tab.text)
            tab = self.tabs[tabs.index(text)]
            tab.click()
            assert_that(text, equal_to(self.current_tab.text), 'Invalid current tab')

    def check_image_url(self, number, url):
        """check url image form search results
        :param number: search results number
        :param url: image url
        """
        with allure.step('check image number "{0}" have url {1}'.format(number, url)):
            assert_that(url, is_in(self.images[number].get_attribute('href')),
                        'Wrong url from first image link')
