from selenium import webdriver


class GetDriver:
    # 声明变量
    __web_driver = None

    # 获取web页面的driver
    @classmethod
    def get_web_driver(cls,url):

        # 判断driver是否为空
        if cls.__web_driver is None:
            # 获取浏览器
            cls.__web_driver = webdriver.Chrome()
            # 最大化浏览器
            cls.__web_driver.maximize_window()
            # 打开url
            cls.__web_driver.get(url)
        # 返回driver
        return cls.__web_driver

    # 结束
    @classmethod
    def quit_web_driver(cls):
        # 判断driver是否不为空
        if cls.__web_driver:
            # 关闭浏览器
            cls.__web_driver.quit()
            # 将driver置空
            cls.__web_driver = None

