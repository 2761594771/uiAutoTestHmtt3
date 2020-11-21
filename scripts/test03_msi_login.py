from time import sleep

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver


class TestMsiLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_web_driver(page.msi_url)
        # 通过统一入口类对象获取PageMsiLogin
        self.msi = PageIn(driver).page_get_PageMsiLogin()
    # 结束
    def teardown_class(self):
        GetDriver.quit_web_driver()

    # 登录测试业务方法
    def test_msi_login(self, username='testid', pwd= 'testpwd123'):
        sleep(1)
        self.msi.page_msi_login(username,pwd)
        print("获取的昵称为",self.msi.page_get_nickname())
