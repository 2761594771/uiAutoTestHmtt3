from page.page_mp_login import PageMpLogin


class PageIn:
    def __init__(self,driver):
        self.driver = driver

    # 获取PageMpLogin页面对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)