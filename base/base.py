import allure
from selenium.webdriver.support.wait import WebDriverWait

from tools.get_log import GetLog

log = GetLog().get_logger()
class Base:
     # 初始化driver
    def __init__(self,driver):
        log.info("正在初始化driver:{}".format(driver))
        self.driver = driver

    # 查找元素  方法封装
    def base_find(self,loc,timeout=30,poll=0.5):
        '''

        :param loc:
        :param timeout:
        :param poll:
        :return:
        '''
        log.info("正在查找:{}元素".format(loc))
        return (WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll).until(lambda x :x.find_element(*loc)))
    # 输入  方法封装
    def base_input(self,loc,value):
        # 获取元素
        ele = self.base_find(loc)

        # 清空文本框
        ele.clear()
        log.info("正在对{}元素执行清空操作".format(loc))
        # 输入操作
        log.info("正在对{}元素执行输入：{} 操作".format(loc,value))
        ele.send_keys(value)

    # 点击  方法封装
    def base_click(self,loc):
        log.info("正在对{}元素执行点击操作".format(loc))
        self.base_find(loc).click()
    # 获取  元素文本封装
    def base_get_text(self,loc):
        log.info("正在对{}元素执行获取文本操作".format(loc))
        return self.base_find(loc).text

    # 截图方法
    def base_get_image(self):
         self.driver.get_screenshot_as_file("./image/err.png")
         # 调用图片写入报告方法
         log.error("断言出错，正在将错误图片写入allure报告")
         self.__base_write_img()

    # 将图片写入报告的方法
    def __base_write_img(self):
         # 获取图片写入文件流
            with open("./image/err.png","rb") as f:
                # allure.attach("错误原因：",f.read(),allure.attach_type.PNG)
                allure.attach("错误原因：",f.read(),allure.attachment_type.PNG)
