

from tools import project_path
import pandas as pd

class GetData:
    Cookie=None
    NoRegTel=pd.read_excel(project_path.test_case_path,sheet_name="init").iloc[0,0]

# setattr(GetCookie,"Cookie","333")  #设置Cookie属性值
# print(hasattr(GetCookie,"Cookie")) #判断是否有Cookie的属性值
# delattr(GetCookie,"Cookie")
# print(hasattr(GetCookie,"Cookie")) #判断是否有Cookie的属性值
# print(getattr(GetCookie,"Cookie")) #获取Cookie属性值

# print(pd.read_excel(project_path.test_case_path, sheet_name="init").iloc[0,0])
