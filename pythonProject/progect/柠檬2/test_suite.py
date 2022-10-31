
import unittest
import HTMLTestRunnerNew
from progect.柠檬2.test_http import TestHttp #类名
from progect.Excel.class_excel import DoExcel
from progect.Excel.class_excel import DoExcel2

# test_data=[{"url":"https://www.vipzhonglian.com/login /","data":{"uname": "17701583363", "upwd": "583363"},"expected":"10001","method":"post"},
#             {"url":"https://www.vipzhonglian.com/login /","data":{"uname": "17701583363", "upwd": "583366"},"expected":"20111","method":"post"},
#             {"url":"https://www.vipzhonglian.com/充值/","data":{"uname": "17701583363", "amoutn": "1000"},"expected":"10001","method":"post"},
#             {"url":"https://www.vipzhonglian.com/充值/","data":{"uname": "17701583363", "amoutn": "-1000"},"expected":"20117","method":"post"}
#             ]

#方法1
test_data =DoExcel("D:\pythonProject\progect\Excel/test1.xlsx","Sheet1").get_data()
suite=unittest.TestSuite()#存储用例
for inem in test_data:
    suite.addTest(TestHttp("test_api",inem["url"],eval(inem["data"]),inem["method"],str(inem["expected"])))


#方法2
t=DoExcel2("D:\pythonProject\progect\Excel/test1.xlsx","Sheet1")
suite2=unittest.TestSuite()#存储用例
for i in range(1,t.max_row+1):
    suite2.addTest(TestHttp("test_api",t.get_data(i,1),t.get_data(i,2),eval(t.get_data(i,3)),str(t.get_data(i,4))))


#方法3 使用装饰类的调用
suite3=unittest.TestSuite()#存储用例
loader=unittest.TestLoader()#创建一个加载器
suite3.addTest(loader.loadTestsFromTestCase(TestHttp))

for inem in test_data:
    suite.addTest(TestHttp("test_api",inem["url"],eval(inem["data"]),inem["method"],str(inem["expected"])))

#执行
with open("test_summer.html","wb") as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title="测试系统V2.0测试报告",
                                             description="测试系统V2.0测试报告第一期会议",
                                            is_thread=False,
                                            retry=0,
                                            save_last_try=True)
    runner.run(suite3)