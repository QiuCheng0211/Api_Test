from tools import project_path  # 引入公共路径的py文件
import pandas as pd

"""映射以及获取需要替换的数据"""


class GetData:
    Cookie = None
    load_id = None
    # 从excel里面拿备用替换数据，参照init表单查看我们这个变量的用处
    NoRegTel = pd.read_excel(project_path.test_case_path, sheet_name="init").iloc[0, 0]  # 表格实际第二行第一个
    normal_tel = pd.read_excel(project_path.test_case_path, sheet_name="init").iloc[1, 0]  # 表格实际第三行第一个
    admin_tel = pd.read_excel(project_path.test_case_path, sheet_name="init").iloc[2, 0]
    loan_member_id = pd.read_excel(project_path.test_case_path, sheet_name="init").iloc[3, 0]
    member_ID = pd.read_excel(project_path.test_case_path, sheet_name="init").iloc[4, 0]
