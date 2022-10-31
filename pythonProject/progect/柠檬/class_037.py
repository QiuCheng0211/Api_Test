
import unittest
from progect.柠檬.class_036 import TestMathMethod
from progect.柠檬 import HTMLTestRunnerNew
suite=unittest.TestSuite()#储蓄用例

#方法一
#执行已下固定的用例
# suite.addTest(TestMathMethod("test_add_two_positive"))#传参方法名  用例名
# suite.addTest(TestMathMethod("test_add_two_zero"))
# suite.addTest(TestMathMethod("test_add_two_negative"))

# 方法二  利用loadTestsFromTestCase执行得是真个类里面的用例
# loader=unittest.TestLoader()#创建一个加载器
# suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))


#方法三 利用loadTestsFromModule加载整个模块
from progect.柠檬 import class_036 #注意导入到模块即可 一般是导入到类名
loader=unittest.TestLoader()#创建一个加载器
suite.addTest(loader.loadTestsFromModule(class_036))

#传统执行
# with open("D:/test.txt","w+",encoding="utf-8") as f:
#     runner=unittest.TextTestRunner(stream=f, verbosity=1)
#     runner.run(suite)

#生成html报告
with open("D:/test.HTML","wb") as f:
    runner=HTMLTestRunnerNew.HTMLTestRunner(
                                            stream=f,
                                            verbosity=2,
                                            title="测试系统V2.0测试报告",
                                            description="测试系统V2.0测试报告第一期会议",
                                            is_thread=False,
                                            retry=0,
                                            save_last_try=True
                                                                )
    runner.run(suite)


