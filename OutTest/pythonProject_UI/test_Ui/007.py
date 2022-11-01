# import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # 启动谷歌，开启与浏览器之间的会话
driver.maximize_window()  # 窗口最大化
driver.get("https://www.baidu.com")  # 访问一个网页

driver.find_element(By.ID,value="kw").send_keys("柠檬班")
driver.find_element(By.ID,value="su").click()

#滚动条处理
 #1找到要滚动到可视区域的元素
WebDriverWait(driver,10,1).until(EC.visibility_of_element_located((By.XPATH,'//a[contains(text(),"软件测试培训机构_专注线上培养软件测试高阶人才")]')))
ele=driver.find_element(By.XPATH,'//a[contains(text(),"软件测试培训机构_专注线上培养软件测试高阶人才")]')

#使用JS进行滚动操作
driver.execute_script("arguments[0].scrollIntoView(false);",ele)    #移动到指定元素位置
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  #移动到底部
driver.find_element(By.XPATH,'//a[contains(text(),"下一页")]').click() #点击下一页

# 日期选项面板  只能选不能输入修改的情况下 先去浏览器F12 Console下面调试好 在拿过来用
# js语句   12306首页，查询日期框
# js = 'var ele=document.getElementById("train_date");ele.readOnly=false;ele.value="2022-12-12"'#先设置属性，在修改值
# driver.execute_script(js) #执行js



