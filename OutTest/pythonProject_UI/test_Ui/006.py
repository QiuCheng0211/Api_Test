import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # 启动谷歌，开启与浏览器之间的会话
driver.maximize_window()  # 窗口最大化
driver.get("https://www.vipzhonglian.com/index/login/index.html")  # 访问一个网页


A=driver.find_element(By.ID,value="kw")
A.send_keys(Keys.CONTROL,"v")
A.send_keys(Keys.ENTER)

