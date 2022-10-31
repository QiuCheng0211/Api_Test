
import  unittest
from ddt import ddt,data
from progect.柠檬2.class_034 import HttpRequest
from progect.柠檬2.get_data import GetData_001
from progect.Excel.class_excel import DoExcel


test_data=DoExcel("test1.xlsx", "Sheet2").get_data()#输入case_id就可控制需要打印那些用例

@ddt#装饰类
class TestHttp(unittest.TestCase):
    def setUp(self):
        pass

    @data(*test_data)
    def test_api(self,item):#正常登录
            res=HttpRequest().http_request(item["url"],eval(item["data"]),item["method"],getattr(GetData_001,"Cookie"))
            if res.cookies:
                setattr(GetData_001,"Cookie",res.cookies )#反射
            try:
                self.assertEqual(str(item["expected"]),res.json()["cood"])
            except AssertionError as e:
                print("test_api's error is{0}".format(e))
                raise e



    def tearDown(self):
         pass

#














