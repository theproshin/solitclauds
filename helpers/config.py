# encoding=utf-8
from configparser import ConfigParser
import os


__all__ = ['Config', ]


class Config():

    instance = None  # for singletone

    def __new__(cls, *args, **kwargs):  # singleton
        if not cls.instance:
            cls.instance = super(Config, cls).__new__(cls)
        return cls.instance

    def __init__(self, path=None, encoding='UTF-8'):
        if not hasattr(self, 'parser'):
            self.__init(path, encoding)

    def __init(self, path, encoding):
        if not path:
            path = os.path.join(os.getcwd(), 'config.ini')
        self.parser = ConfigParser()
        self.parser.read(path, encoding=encoding)

    def get(self, section, option):
        """get option form section
        :param section: section name
        :param option: option name
        """

        return self.parser.get(section, option)

    def get_test_data(self, option):
        """get option from section test_data
        :param option: option name
        """

        return self.parser.get('test_data', option)
