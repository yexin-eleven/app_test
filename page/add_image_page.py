from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class Add_image_page(BaseAction):
    Edit_name = By.XPATH,'//*[@text="姓名"]'

    Edit_phone = By.XPATH,'//*[@text="电话"]'

    Back_btn = By.CLASS_NAME,'android.widget.ImageButton'

    def  input_name(self,text):
        self.input(self.Edit_name,text)

    def input_phone(self,num):
        self.input(self.Edit_phone,num)

    def click_back_btn(self):
        self.click(self.Back_btn)