# -*- coding: UTF-8 -*-

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