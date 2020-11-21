import document as document

import page
from base.web_base import WebBase


class PageMsiLogin(WebBase):
    # 输入用户名
    def page_input_username(self,username):
        self.base_input(page.msi_username,username)
    # 输入密码
    def page_input_pwd(self,pwd):
        self.base_input(page.msi_pwd,pwd)
    # 点击登录按钮
    def page_click_longinButton(self):
        # 设置js
        js = "document.getElementById('inp1').disabled = false"
        self.driver.execute_script(js)
        # 调用点击操作
        self.base_click(page.msi_login_btn)
    # 获取昵称 封装
    def page_get_nickname(self):
        self.base_get_text(page.msi_nickname)
    # 组合 后台管理登录业务方法
    def page_msi_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_longinButton()