from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()           # 启动谷歌，开启与浏览器之间的会话
driver.get("https://www.baidu.com")   # 访问一个网页

A = driver.find_element(By.ID, value="kw")                                    # 通过id定位
print(A.get_attribute("class"))                                        # 获取class的值

driver.find_element(By.CLASS_NAME, value="s_ipt")                              # 通过class定位
driver.find_element(By.NAME, value="wd")                                        # 通过name定位
driver.find_element(By.TAG_NAME, value="input")                                 # 通过标签名定位
driver.find_element(By.LINK_TEXT, value="更多产品")                               # 文本精确匹配
driver.find_element(By.PARTIAL_LINK_TEXT, value="更多产品")                       # 文本模糊匹配

# 绝对定位 以/开头 非常依赖于页面的顺序和位置
# 相对定位 以//开头 不依赖页面的顺序和位置。只看 整个页面有么有符合表达式的元素
# //标签名称[@属性名称=值 and @属性名称=值]  标签名称可以的*代替

# 如果遇到两个一摸一样，常用方法无法做到精确定位的时候，可以使用“层级定位 ”例如：//div[@id="u1"]//a[@id="s-top-loginbtn"]
# 文本定位：//div[@id="s-top-left"]//a[text()="地图"]
# contains(@属性名称/text(),文本内容)包含     //input[contains(@class,"s_") ]
# 轴定位

driver.find_element(By.XPATH, value='//*[@id="kw"]').click() # 相对定位

# Id>name>class


"""
.send_keys()                输入值
.click()                    点击操作
.clear()                    清空内容
.submit()                   提交表单模拟回车
.maximize_window()            #窗口最大化
.back()                       #回退上一页
.forward()                    #回到下一页
.refresh()                    #刷新页面
.title                        #获取标题
.current_url                  #获取网址
.current_window_handle        #窗口的id

"""
