import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # 启动谷歌，开启与浏览器之间的会话
# driver.implicitly_wait(15)  # 全局等待 影性等待
driver.get("https://ke.qq.com/")  # 访问一个网页
driver.maximize_window()  # 窗口最大化
driver.find_element(By.ID, value='js_login').click()

id = "TANGRAM__PSP_11__submit"

# 显性等待类(driver,等待时间,轮循周期) until 判断负荷(元素可见)
# WebDriverWait(driver,10,1).until(EC.visibility_of_element_located((By.ID,id)))

# 切换至iframe页面 三种方法
# driver.switch_to.frame('frame')  #name值
# driver.switch_to.frame(1)  #index 下标
driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@scrolling="no" and @width="368px"]'))  # webelement
time.sleep(0.5)
driver.find_element(By.ID, value='switcher_plogin').click()

# 切换至iframe页面判断+等待拓展
# WebDriverWait(driver,10,1).until(EC.frame_to_be_available_and_switch_to_it('frame')) #frame  是name值
# time.sleep(0.5)

# 从iframe回到默认的页面中
driver.switch_to.default_content()

# 遇到多层从iframe时候，从iframe返回上一层从iframe。
driver.switch_to.parent_frame()

# 窗口切换  见 004文件

