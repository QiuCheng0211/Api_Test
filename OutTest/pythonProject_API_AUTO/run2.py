
 import unittest
import HTMLTestRunnerNew
from tools.project_path import *
from tools.test_http_request import TestHttpRequest

suite=unittest.TestSuite()  #创建测试套件  存储用例
#suite.addTest(TestHttpRequest("test_api"))#测试类的实例   在存储用例对象里添加测试用例
loader=unittest.TestLoader()#创建一个加载器
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
#执行用例
with open(test_report_path,"wb") as file:
    #runner=unittest.TextTestRunner()
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                                verbosity=2,
                                                title="测试系统V2.0测试报告",
                                                description="测试系统V2.0测试报告第一期会议",
                                                is_thread=False,
                                                retry=0,
                                                save_last_try=True)
    runner.run(suite)