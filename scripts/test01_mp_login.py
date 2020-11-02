import pytest

from page.page_in import PageIn
from tools.get_log import GetLog
from tools.read_yaml import read_yaml
from tools.get_driver import GetDriver
import page

log = GetLog().get_logger()
class TestMpLogin:
     #初始化
    def setup_class(self):
        #获取driver
        driver = GetDriver.get_web_driver(page.mp_url)
        # 通过统一入口类获取PageMpLongin对象
        # self.mp = PageIn(driver).page_get_PageMpLogin()
        self.mp = PageIn(driver).page_get_PageMpLogin()

    # 关闭浏览器
    def teardown_class(self):
        GetDriver.quit_web_driver()

    # 测试业务方法
    @pytest.mark.parametrize("username,code,expect_result", read_yaml("mp_login.yaml"))
    def test_mp_login(self, username, code, expect_result):
        # 调用登录业务方法
        self.mp.page_mp_login(username, code)
        try:
            # 断言
            assert expect_result == self.mp.page_get_nickname()
            print(self.mp.page_get_nickname())
        except Exception as e:
            # 打印异常
            log.error("断言出错，错误信息:{}".format(e))
            print("异常是：",e)
            # 截图
            self.mp.base_get_image()
            # 抛出异常
            raise



