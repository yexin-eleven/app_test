from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MessagePage(BaseAction):
    #新建短信按钮

    new_message_btn = By.ID,"com.android.mms:id/action_compose_new"

    def click_new_message_btn(self):
        self.click(self.new_message_btn)