from selenium.webdriver.common.by import By

class LoginPageLocators:
    # 元素定位区域
    name_id = (By.ID, "uname")  # 用户名输入框
    pwd_id = (By.ID, "upwd")  # 密码输入框
    login_id = (By.ID, "submit_login")  # 登录按钮
    # 错误提示框
    errorMgs_from_loginArea = (By.XPATH, '//div[@class="layui-layer layui-layer-dialog layui-layer-border layui-layer-msg"]')

