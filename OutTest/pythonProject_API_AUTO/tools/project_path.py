"""
准们读取路径的值
"""
import os

project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
#测试用例的路径
test_case_path=os.path.join(project_path,"test_data","test_data.xlsx")
#测试报告的路径
test_report_path=os.path.join(project_path,"test_resuit","html_report","test_api.html")
#配置文件路径
case_config_path=os.path.join(project_path,"conf","case.config")

print(test_case_path)
print(test_report_path)
print(case_config_path)

