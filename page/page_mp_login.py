from time import sleep

from base.base import Base
import page
from tools.get_log import GetLog

log = GetLog().get_logger()
class PageMpLogin(Base):

    #  输入用户名 方法 封装
    def page_input_username(self,username):
        self.base_input(page.mp_username,username)
    # 输入验证码方法 封装
    def page_input_code(self,code):
        self.base_input(page.mp_code,code)

    # 点击 登录按钮封装
    def page_click_login_btn(self):
        self.base_click(page.mp_login_btn)

    # 获取昵称 封装
    def page_get_nickname(self):
        return  self.base_get_text(page.mp_nickname)

    # 登录流程方法组合
    def page_mp_login(self,username,code):
        log.info("正在调用自媒体登录业务方法，用户名：{},密码：{}".format(username,code))
        self.page_input_username(username)
        self.page_input_code(code)
        sleep(1)
        self.page_click_login_btn()

