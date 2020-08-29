
# 用户名
from selenium.webdriver.common.by import By

mp_username = (By.CSS_SELECTOR,"[placeholdeer='请输入手机号']")
# 验证码
mp_code = (By.CSS_SELECTOR,"[placeholder='验证码']")
# 登录按钮
mp_login_btn = (By.CSS_SELECTOR,".el-button--primary")
# 昵称
mp_nickname = (By.CSS_SELECTOR,".user-name")