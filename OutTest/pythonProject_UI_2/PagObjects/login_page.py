import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from PageLocators.loginpage_locators import LoginPageLocators as loc
from common.basepage import BasePage

class Log_Page(BasePage):

    # 登录操作
    def login(self, username, passwd, remeber_user=True):
        # 输入用户名#输入密码
        # 点击登录
        doc="登陆页面_登录功能"

        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.name_id))
        # self.driver.find_element(*loc.name_id).send_keys(username)
        # self.driver.find_element(*loc.pwd_id).send_keys(passwd)
        # self.driver.find_element(*loc.login_id).click()

        # self.wait_eleVisible(locator=loc.name_id, doc=doc)
        self.wait_eleVisible(loc.name_id, doc=doc)
        self.input_text(loc.name_id,username,doc)
        self.input_text(loc.pwd_id, passwd, doc)
        self.click_element(loc.login_id,doc)


    # 注册入口
    def register(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//a[text()="去注册"]')))
        self.driver.find_element(By.XPATH, '//a[text()="去注册"]').click()

    # 获取错误提示信息 —— 登陆区域
    def get_errorMsg_from_loginArea(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.errorMgs_from_loginArea))
        return self.driver.find_element(*loc.errorMgs_from_loginArea).text
