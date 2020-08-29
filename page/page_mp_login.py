
from base.base import Base
import page

class PageMpLogin(Base):

    #  输入用户名 方法 封装
    def page_input_username(self):
        self.page.mp_username
    # 输入验证码方法 封装
    def page_input_code(self):
        pass

    # 点击 登录按钮封装
    def page_click_login_btn(self):
        pass

    # 获取昵称 封装
    def page_get_nickname(self):
        pass

