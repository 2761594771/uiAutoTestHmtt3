from page.page_mp_login import PageMpLogin
from page.page_mp_article import PageMpArticle

class PageIn:
    def __init__(self,driver):
        self.driver = driver

    # 获取PageMpLogin页面对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)
    # 获取PageMpArticle页面对象
    def page_get_PageMpArticle(self):
        return PageMpArticle(self.driver)