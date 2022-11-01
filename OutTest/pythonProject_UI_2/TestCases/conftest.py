
from TestDatas import Commom_Datas as CD
from selenium import webdriver
from PagObjects.login_page import Log_Page
import pytest

#声明他是一个fixture

@pytest.fixture(scope="class")
def access_web():
    #前置操作
    driver = webdriver.Chrome()
    driver.get(CD.web_login_url)  # url网址
    driver.maximize_window()  # 窗口最大化
    lg = Log_Page(driver)
    yield
    #后置操作
    driver.quit()

def refresh_page():
    #前置操作
    yield
    #后置操作
    # driver.refresh()  # 每条用例执行后刷新一次