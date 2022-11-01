import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # 启动谷歌，开启与浏览器之间的会话
driver.get("https://www.baidu.com")  # 访问一个网页
driver.maximize_window()  # 窗口最大化
driver.find_element(By.ID,value="kw").send_keys("柠檬班")
driver.find_element(By.ID,value="su").click()


WebDriverWait(driver,10,1).until(EC.visibility_of_element_located((By.XPATH,'//a[contains(text(),"百度百科")]')))
driver.find_element(By.XPATH,'//a[contains(text(),"百度百科")]').click()
time.sleep(0.5)


#step1:获取窗口的总数以及句炳 新打开窗口位数最后一个
handles=driver.window_handles
print(handles)

#获取当前窗口句柄
handles1=driver.current_window_handle
print(handles1)

#窗口切换
driver.switch_to.window(handles[-1])

#第二个页面经行操作
WebDriverWait(driver,30,1).until(EC.visibility_of_element_located((By.XPATH,'//span[contains(text(),"收藏")]')))
driver.find_element(By.XPATH,'//span[contains(text(),"收藏")]').click()

#获取当前窗口句柄
handles2=driver.current_window_handle
print(handles2)

# WebDriverWait(driver,10).until(EC.alert_is_present())
# #小弹框处理  alert切换  不是html页面元素
# alert=driver.switch_to.alert
# alert.accept()   #接受
# alert.dismiss()  #拒绝
# print(alert.text) #获取打印弹窗的文本
