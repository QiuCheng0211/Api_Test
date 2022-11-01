import unittest
from selenium import webdriver
from PagObjects.login_page import Log_Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IndexPage:

    def __init__(self,driver):
        self.driver=driver

    def isExist_logout_ele(self):
        #如果存在就返回Ture，如果不存在，就返回False
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="nexDL_Bod"]//span[text()="我的账户"]')))
            return True
        except:
            return False





#  //div[@class="layui-layer layui-layer-dialog layui-layer-border layui-layer-msg"]//div[text()="用户名不能为空"] 用户名空
#  //div[@class="layui-layer layui-layer-dialog layui-layer-border layui-layer-msg"]//div[text()="用户名/手机不存在"]  手机号错误
#  //div[@class="layui-layer layui-layer-dialog layui-layer-border layui-layer-msg"]//div[text()="用户名/手机不存在或密码不正确"]  密码错误
#  //div[@class="layui-layer layui-layer-dialog layui-layer-border layui-layer-msg"]//div[text()="密码不能为空！"]  密码为空
#  //div[@class="layui-layer layui-layer-dialog layui-layer-border layui-layer-msg"]//div[text()="密码长度不得小于6位数！"]  密码低于6位

