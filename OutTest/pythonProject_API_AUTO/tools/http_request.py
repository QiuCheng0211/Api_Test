import requests
from tools.my_log import MyLog

my_logger=MyLog()

class HttpRequest:

    @staticmethod
    def http_request(url, data, http_method, cookie=None):
        try:
            if http_method.upper() == "GET":
                res = requests.get(url, data, cookies=cookie)
            elif http_method.upper() == "POST":
                res = requests.post(url, data, cookies=cookie)
            else:
                my_logger.info("请输入正确的请求方法")
        except Exception as e:
            my_logger.error("请求报错了{}".format(e))
            raise e
        return res  #返回消息实体

""""
            已下均不被其他导入import使用
"""

if __name__ == '__main__':
    #注册
    register_url = "https://www.vipzhonglian.com/zhuce /"
    register_data = {"uname": "17701583363", "upwd": "583363"}
    #登录
    login_url = "https://www.vipzhonglian.com/login/"
    login_data = {"uname": "17701583363", "upwd": "583363"}
    #充值
    recharge_url = "https://www.vipzhonglian.com/chongzhi /"
    recharge_data = {"uname": "17701583363", "upwd": "583363"}

    login_res = HttpRequest().http_request(login_url, login_data, "get")
    recharge_res = HttpRequest().http_request(recharge_url, recharge_data, "post", login_res.cookies)
    print("充值的结果：{}".format(recharge_res.json()))

