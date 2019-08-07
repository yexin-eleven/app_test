from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewmessagePage(BaseAction):
    #接收者文本框
    js = By.ID,'com.android.mms:id/recipients_editor'
    #键入信息文本框
    jr = By.ID,'com.android.mms:id/embedded_text_editor'
    #发送按钮
    fs = By.ID,'com.android.mms:id/send_button_sms'

    def input_js(self,text):
        self.input(self.js,text)

    def input_jr(self,text):
        self.input(self.jr,text)

    def click_fs(self):
        self.click(self.fs)
