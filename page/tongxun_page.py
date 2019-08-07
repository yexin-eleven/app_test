from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class Tongxun_list_page(BaseAction):
    Image_btn = By.ID,"com.android.contacts:id/floating_action_button"

    def click_Image_btn(self):
        self.click(self.Image_btn)