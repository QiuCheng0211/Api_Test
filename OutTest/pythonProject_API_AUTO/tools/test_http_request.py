import unittest
from tools.http_request import HttpRequest
from tools.get_data import GetData
from ddt import ddt,data#列表嵌套列表，或者列表嵌套字典
from tools.do_excel import DoExcel
from tools.project_path import *
from tools.my_log import MyLog

my_logger=MyLog()
test_data=DoExcel.get_data(test_case_path)#执行用例数据来源

@ddt#装饰测试类
class TestHttpRequest(unittest.TestCase):
    def setUP(self):
        pass

    @data(*test_data)#装饰测试用例  托一层外套 将test_data传入item
    def test_api(self,item):
        res=HttpRequest.http_request(item, eval(item["data"]),item["http_method"], getattr(GetData, "Cookie"))
        if res.cookies:
            setattr(GetData,"Cookie",res.cookies)#利用反射存储cookie值

        try:
            self.assertEqual(str(item["expected"]), res.json()["cood"]) #断言结果
            TestResult="PASS"#成功
        except Exception as e:
            TestResult = "Failed" #失败
            my_logger.info("执行的错误结果是：{}".format(e))
            raise e
        finally:#不管对错，对里面的代码都要执行
            DoExcel.write_back(test_case_path, item["sheet_name"], item["case_id"]+1, str(res.json()), TestResult)#结果写回
            my_logger.error("获取到的结果是:{}".format(res.json()))
    def tearDown(self):
        pass
