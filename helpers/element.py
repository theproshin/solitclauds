# encoding=utf-8


__all__ = ['Element', 'Input']


class Element(object):

    def __init__(self, by, value, name):
        """init
        :param by: strategy search
        :param value: locator element
        :param name: name element (for logging feature and debug)
        """

        self.by = by
        self.value = value
        self.name = name
        self.driver = None

    def get_webelement(self):
        """get webelement"""

        return self.driver.find_element(self.by, self.value)

    def click(self):
        """click"""

        self.get_webelement().click()

    def send_keys(self, text):
        """type text
        :param text: text for input
        """
        self.get_webelement().send_keys(text)

    def clear(self):
        """clear text in element(input)"""

        self.get_webelement().clear()

    @property
    def text(self):
        """get visible text element"""

        return self.get_webelement().text

    def get_attribute(self, attribute):
        """get attribute form element
        :param attribute: attribute name
        """

        return self.get_webelement().get_attribute(attribute)


class Input(Element):

    @property
    def text(self):
        """get value(text) input"""

        return self.get_attribute('value')
