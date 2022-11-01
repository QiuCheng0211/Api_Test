from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # 启动谷歌，开启与浏览器之间的会话
driver.maximize_window()  # 窗口最大化
driver.get("http://192.168.0.33:8080/zz/u/login.shtml")  # 访问一个网页
# 输入账户
driver.find_element(By.XPATH,value='//input[@placeholder="请输入账号"]').send_keys("admin")
# 输入密码
driver.find_element(By.XPATH,value='//input[@placeholder="请输入密码"]').send_keys("sojson")
# 点击登录
driver.find_element(By.XPATH,value="/html/body/div/div/div/div[1]/div[2]/div[2]/div/form/div[4]/button").click()
# 等待页面出现 设备管理元素
# 显性等待类(driver,等待时间,轮循周期) until 判断负荷(元素可见)
WebDriverWait(driver, 20,1).until(EC.visibility_of_element_located((By.XPATH,'//li[@class="menu-dropdown mega-menu-dropdown"]//a[@href="javascript:;"]')))
# 获取 设备管理元素
ele=driver.find_element(By.XPATH,value='//li[@class="menu-dropdown mega-menu-dropdown"]//a[@href="javascript:;"]')
# 加入鼠标悬浮操作
ActionChains(driver).move_to_element(ele).perform()
# 获取鼠标悬浮后德操作定位元素，点击操作
driver.find_element(By.XPATH,value="/html/body/div[1]/div[1]/div/div/div/div/div/div[2]/div/div/ul/li[11]/ul/li/div/div/div[1]/ul/li[8]/a").click()


"""

模组送检
电表联调测试
6600
三星学习负荷辨识
TDTU改造
电瓶车时间

"""