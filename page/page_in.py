from page.page_mp_login import PageMpLogin
from page.page_mp_article import PageMpArticle
from page.page_msi_login import PageMsiLogin


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin页面对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)

    # 获取PageMpArticle页面对象
    def page_get_PageMpArticle(self):
        return PageMpArticle(self.driver)

    # 获取PageMsiLogin页面对象
    def page_get_PageMsiLogin(self):
        return PageMsiLogin(self.driver)
