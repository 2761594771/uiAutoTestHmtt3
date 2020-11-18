from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base


class WebBase(Base):
    """以下为web项目专属方法"""
    # 根据显示的文本点击指定的元素
    def web_base_click_element(self,placeholder_text,click_text):
        # 1.点击父选框
        loc = By.CSS_SELECTOR, " [placeholder = '{}'] ".format(placeholder_text)
        self.base_click(loc)
        # 暂停
        sleep(1)
        # 点击包含显示文本的元素
        loc = By.XPATH, "//*[text()='{}']".format(click_text)
        self.base_click(loc)
