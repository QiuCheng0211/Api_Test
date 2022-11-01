import requests
from tools.my_log import MyLog

my_logger = MyLog()


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
        return res  # 返回消息实体
