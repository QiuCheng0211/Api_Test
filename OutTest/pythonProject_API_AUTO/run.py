from tools.http_request import HttpRequest
from tools.do_excel import DoExcel
from tools.get_data import GetCookie


'''
不使用excel处理数据
test_data = [{"url": "https://www.vipzhonglian.com/login/",
            "data": {"uname": "17701583363", "pwd": "583363"},"title": "正常登录", "http_method":"get"},
            {"url": "https://www.vipzhonglian.com/login/",
            "data": {"uname": "17701583363", "pwd": "583366"},"title": "密码错误", "http_method":"post"}]
'''
COOKLE=None

def run(test_data,sheet_name):
    global COOKLE
    for item in test_data:
        print("正在测试的用例是{}".format(item["title"]))
        res=HttpRequest.http_request(item["url"],eval(item["data"]) ,item["http_method"],item["title"],COOKLE)

        if COOKLE:
            COOKLE=res.cookies
        print("请求的结果是{}".format(res.json()))
        DoExcel.write_back("test_data/test_data.xlsx",sheet_name,item["case_id"]+1,str(res.json()))

test_data=DoExcel.get_data("test_data/test_data.xlsx","recharge")

run(test_data,"recharge")