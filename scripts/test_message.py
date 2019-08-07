import time

import pytest

from base.base_driver import init_driver
from page.page import Page


class TestMessage:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    # @pytest.mark.parametrize(('phone','text'),[('18812345678','by,by'),('13312345678','hello')])
    # def test_send_message(self,phone,text):
    #     self.page.message_list().click_new_message_btn()
    #
    #     self.page.new_message_list().input_js(phone)
    #
    #     self.page.new_message_list().input_jr(text)
    #
    #     self.page.new_message_list().click_fs()

    @pytest.mark.parametrize(('text','num'),[('wangwu','18812345678'),('lili','18999999999')])
    def test_add_new_people(self,text,num):
        self.page.tongxun_list().click_Image_btn()
        self.page.add_image_list().input_name(text)
        self.page.add_image_list().input_phone(num)
        self.page.add_image_list().click_back_btn()

