

from selenium.webdriver.support.wait import WebDriverWait


class Base:
     # 初始化driver
    def __init__(self,driver):
        self.driver = driver

    # 查找元素  方法封装
    def base_find(self,loc,timeout=30,poll=0.5):
        '''

        :param loc:
        :param timeout:
        :param poll:
        :return:
        '''
        return (WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll).until(lambda x :x.find_element(*loc)))
    # 输入  方法封装
    def base_input(self,loc,value):
        # 获取元素
        ele = self.base_find(loc)
        # 清空文本框
        ele.clear()
        # 输入操作
        ele.send_keys(value)
    # 点击  方法封装
    def base_click(self,loc):
        self.base_find(loc).click()
    # 获取  元素文本封装
    def base_get_text(self,loc):
        return self.base_find(loc).text