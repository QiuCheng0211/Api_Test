import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()  # 启动谷歌，开启与浏览器之间的会话
driver.maximize_window()  # 窗口最大化
driver.get("https://www.baidu.com")  # 访问一个网页

#1先找到鼠标要操作的元素
ele=driver.find_element(By.XPATH,value='//div[@id="u1"]//span[@name="tj_settingicon"]')

# #2实例化 ActionChains类
# ac = ActionChains(driver)
#
# #3将鼠标操作添加到actions中
# ac.move_to_element(ele)
#
# #4调用perform()来执行鼠标操作
# ac.perform()
#
# 第二种操作方法
ActionChains(driver).move_to_element(ele).perform()

# 定位鼠标悬浮才出现的列表 鼠标一走就不见了 小技巧  按住不松开ctrl+shift+c  鼠标放置悬浮区域 就可以看到元素定位
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//span[text()='高级搜索']")))
driver.find_element(By.XPATH, "//span[text()='高级搜索']").click()

"""
以下是针对select元素下拉列表处理
#select类
#1找到select元素
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="c-select-dropdown adv-ft-dropdown"]//div[@class="c-select-dropdown-list"]')))
select_ele=driver.find_element(By.XPATH, '//div[@class="c-select-dropdown adv-ft-dropdown"]//div[@class="c-select-dropdown-list"]')

#2实例化Select类
s=Select(select_ele)   #必须是select元素标签  而不是div标签

#3选择下拉表值
#方式一:下标从0开始
s.select_by_index(4)
#方式二:value值
s.select_by_value("all")
#方式三:文本内容
s.deselect_by_visible_text("Adobe Acrobat PDF (.pdf)")

"""