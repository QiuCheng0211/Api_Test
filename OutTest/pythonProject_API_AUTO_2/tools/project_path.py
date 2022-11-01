"""
专门读取路径的值
"""
import os

project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]  # 读取到该项目阶段的路劲
# 测试用例的路径
test_case_path = os.path.join(project_path, "test_data", "test_data.xlsx")  # 在该阶段项目下继续读取\test_data\test_data.xlsx
# 测试报告的路径
test_report_path = os.path.join(project_path, "test_resuit", "html_report","test_api.html")  # 在该阶段项目下继续读取\test_resuit\html_report\test_api.html
# 配置文件路径
case_config_path = os.path.join(project_path, "conf", "case.config")  # 在该阶段项目下继续读取\conf\case.config

print(test_case_path)
print(test_report_path)
print(case_config_path)

"""
python自动化接口测试里面经常用到的两个os.path方法
os.path.split(path ) : 把路径分割成 dirname（路径名） 和 basename（文件名），返回一个元组；
os.path.realpath(path)：获取path的绝对路径；
os.path.realpath(__file__)：获取realpath方法所在脚本的绝对路径
举例如下：
path = os.path.split(os.path.realpath(__file__))[0]
这里os.path.realpath(__file__) 返回当前脚本的绝对路径（比如是C:/users/automation/test.py）；
os.path.split( ):将上面得到的绝对路径进行分割得到一个元组['C:/users/automation/', 'test.py']
在后面加上一个[0]，即得到了‘C:/users/automation/’
"""
