import unittest
from selenium import webdriver
from PagObjects.login_page import Log_Page
from PagObjects.index_page import IndexPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestDatas import Commom_Datas as CD
from TestDatas import Login_Datas as LD
import ddt
import pytest

def test_demo():
    pass

@ddt.ddt()
class TestLogin(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(CD.web_login_url)  # url网址
        cls.driver.maximize_window()  # 窗口最大化
        cls.lg = Log_Page(cls.driver)
    #
    # @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    #
    # def setUp(self):
    #     # 前置 访问登陆页面
    #     pass

    def tearDown(self):
        # 后置
        self.driver.refresh()#每条用例执行后刷新一次

    # 正常用例  登录成功
    @pytest.mark.smoke
    def test_login_1_success(self):
        # 步骤  输入用户名  密码 点击登录
        self.lg.login(LD.success_data["user"], LD.success_data["passwd"])
        # 断言  首页当中 能否找到我的账户这个元素  //div[@class="nexDL_Bod"]//span[text()="我的账户"]
        self.assertTrue(IndexPage(self.driver).isExist_logout_ele())


    # 异常用例  手机号格式不正确(用户名空 手机号错误 密码错误 密码为空 密码低于6位)  ddt
    @ddt.data(*LD.phone_data)
    def test_login_0_user_wrongFormat(self, data):
        # 步骤  输入用户名  密码 点击登录
        self.lg.login(data["user"], data["passwd"])
        # 断言  登陆页面 提示：请输入正确的手机号
        # 登陆页面 获取提示框文本内容
        # 比对文本内容 与 期望的值 是否相等
        self.assertEqual(self.lg.get_errorMsg_from_loginArea(), data["check"])


        # 异常用例——未注册手机号
        # 异常用例——错误的密码
        # 异常用例——不输入密码
    #  //div[@class="layui-layer layui-layer-dialog layui-layer-border layui-layer-msg"]//div[text()="用户名不能为空"] 用户名空
    #  //div[@class="layui-layer layui-layer-dialog layui-layer-border layui-layer-msg"]//div[text()="用户名/手机不存在"]  手机号错误
    #  //div[@class="layui-layer layui-layer-dialog layui-layer-border layui-layer-msg"]//div[text()="用户名/手机不存在或密码不正确"]  密码错误
    #  //div[@class="layui-layer layui-layer-dialog layui-layer-border layui-layer-msg"]//div[text()="密码不能为空！"]  密码为空
    #  //div[@class="layui-layer layui-layer-dialog layui-layer-border layui-layer-msg"]//div[text()="密码长度不得小于6位数！"]  密码低于6位
