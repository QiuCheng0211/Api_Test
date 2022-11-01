
import  unittest
from progect.柠檬.class_034 import HttpRequest
from progect.柠檬.get_data import GetData_001


#解除依赖关联：1,写到setup里面，每次使用就是请求一次 2,使用全局变量 3,使用映射

# COOKLE=None#全局变量

class TestHttp(unittest.TestCase):
    def setUp(self):
        #登录
        self.login_url = "https://www.vipzhonglian.com/login /"
        # self.login_data = {"uname": "17701583363", "upwd": "583363"}
        self.recharge_url = "https://www.vipzhonglian.com/充值/"                                  #充值url
        # self.cookies=HttpRequest().http_request(self.login_url,self.login_data,"get").cookies    #获取登陆后的cookies
        # print("setup函数里面登陆后产生的cookies是:{0}".format(self.cookies))

    def test_login_normal(self):#正常登录
        # global COOKLE #声明全局变量
        data = {"uname": "17701583363", "upwd": "583363"}
        res=HttpRequest().http_request(self.login_url,data,"get")
        if res.cookies:#如果cookies有值就更新COOKLE
            # COOKLE=res.cookies #更新全局变量
            setattr(GetData_001,"Cookie",res.cookies )
        try:
            self.assertEqual("10000",res.json()["cood"])
        except AssertionError as  e:
            print("test_login_normal's error is{0}".format(e))
            raise e

    def test_login_wrong_pwd(self):#密码输入错误 登录
        data = {"uname": "17701583363", "upwd": "583366"}
        res=HttpRequest().http_request(self.login_url,data,"get")
        try:
            self.assertEqual("10111",res.json()["cood"])
        except AssertionError as  e:
            print("test_login_wrong_pwd's error is{0}".format(e))
            raise e

    def test_recharge_normal(self):#正常充值
        #global COOKLE  # 声明全局变量
        recharge_data = {"uname": "17701583363", "amoutn": "1000"}
        res=HttpRequest().http_request(self.recharge_url,recharge_data,"get",getattr(GetData_001,"Cookie") )
        try:
            self.assertEqual("10001",res.json()["cood"])
        except AssertionError as e:
            print("test_recharge_normal's error is{0}".format(e))
            raise e

    def test_recharge_negative(self):#充值负数
        # global COOKLE  # 声明全局变量
        recharge_data = {"uname": "17701583363", "amoutn": "-1000"}
        res=HttpRequest().http_request(self.recharge_url,recharge_data,"get",getattr(GetData_001,"Cookie"))
        try:
            self.assertEqual("10117",res.json()["cood"])
        except AssertionError as e:
            print("test_recharge_negative's error is{0}".format(e))
            raise e

    def tearDown(self):
         pass















