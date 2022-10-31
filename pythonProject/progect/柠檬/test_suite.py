




import unittest
import HTMLTestRunnerNew
from progect.柠檬 import test_http


suite=unittest.TestSuite()#存储用例

loader=unittest.TestLoader()#加载用例
suite.addTest(loader.loadTestsFromModule(test_http))#按模块名加载用例去储存

#执行
with open("test_summer.html","wb") as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title="测试系统V2.0测试报告",
                                            description="测试系统V2.0测试报告第一期会议",
                                            is_thread=False,
                                            retry=0,
                                            save_last_try=True)
    runner.run(suite)

