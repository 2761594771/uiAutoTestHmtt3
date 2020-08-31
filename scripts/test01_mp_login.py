from page.page_in import PageIn
from tools.get_driver import GetDriver
import page

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
    def test_mp_login(self,username="13812345678",code="246810"):
        # 调用登录业务方法
         self.mp.page_mp_login(username,code)
        #断言
         print("昵称为 ",self.mp.page_get_nickname())


