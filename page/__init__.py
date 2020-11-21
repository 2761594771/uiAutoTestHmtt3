

from selenium.webdriver.common.by import By


'''以下为黑马头条号系统 登录模块 元素配置信息'''
# 用户名
mp_username = (By.CSS_SELECTOR, "[placeholder='请输入手机号']")
# 验证码
mp_code = (By.CSS_SELECTOR, "[placeholder='验证码']")
# 登录按钮
mp_login_btn = (By.CSS_SELECTOR, ".el-button--primary")
# 昵称
mp_nickname = (By.CSS_SELECTOR,".user-name")

'''以下为黑马头条、后台管理系统url'''
mp_url = "http://ttmp.research.itcast.cn/#/login"
msi_url= "http://ttmis.research.itcast.cn/#"


'''以下是黑马头条web项目，内容管理模块 元素配置信息'''
# 内容管理
mp_content_manage = By.XPATH, "//*[text()= '内容管理']/.."
# 发布文章
mp_publish_article = By.XPATH, "//*[contains(text(), '发布文章')]"
# 文章title
mp_title = By.CSS_SELECTOR, "[placeholder='文章名称' ]"
# 文章内容
mp_content = By.CSS_SELECTOR, "#tinymce"
# iframe
mp_iframe = By.CSS_SELECTOR, "#publishTinymce_ifr"
# 封面
mp_cover = By.XPATH, "//*[text() = '自动']"
# 发表按钮
mp_submit = By.XPATH, "//*[text()='发表']/.."
# 结果
mp_result = By.XPATH, "//*[contains(text(),'新增文章成功')]"

"""以下是后台管理系统"""
msi_username = By.CSS_SELECTOR, "[placeholder = '用户名']"
msi_pwd = By.CSS_SELECTOR, "[placeholder = '密码']"
msi_login_btn = By.ID, "#inp1"
msi_nickname = By.CSS_SELECTOR, ".user_info"