# encoding=utf-8
from page_object.main_page import MainPage
from helpers import browser, Config


config = Config()


def test_google_for_solit_clouds(browser):
    """Check google for SolitClouds"""

    main_page = MainPage(browser)
    main_page.open(config.get_test_data('site'), config.get_test_data('title'))
    main_page.search(config.get_test_data('search_text'))
    href = main_page.check_result_url(0, config.get_test_data('test_url'))
    main_page.select_tab_by_text('Картинки')
    main_page.check_image_url(0, config.get_test_data('test_url'))
    main_page.select_tab_by_text('Все')
    main_page.check_result_url(0, href, contains=False)
