from base.base_driver import init_driver
from page.add_image_page import Add_image_page
from page.message_page import MessagePage
from page.new_message_page import NewmessagePage
from page.tongxun_page import Tongxun_list_page


class Page:
    def __init__(self,driver):
        self.driver = driver

    def message_list(self):
        return MessagePage(self.driver)

    def new_message_list(self):
        return NewmessagePage(self.driver)

    def tongxun_list(self):
        return Tongxun_list_page(self.driver)

    def add_image_list(self):
        return Add_image_page(self.driver)