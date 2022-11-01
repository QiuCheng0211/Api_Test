from selenium import webdriver
# 设置你自己的chormedriver存放路径
# driver_path=r"D:\Install_Software\python3.9\chromedriver.exe"
# driver=webdriver.Chrome(executable_path=driver_path)
# driver.get("https://www.baidu.com")
# print (driver.page_source)

driver=webdriver.Chrome()           # 启动谷歌，开启与浏览器之间的会话
driver.get("https://www.baidu.com")  # 访问一个网页
# driver.maximize_window()            # 窗口最大化
# driver.get("https://www.taobao.com") # 访问一个网页
# driver.back()                       # 回退上一页
# driver.forward()                    # 回到下一页
# driver.refresh()                    # 刷新页面
#
# print(driver.title)                 # 获取标题
# print(driver.current_url)           # 获取网址
# print(driver.current_window_handle) # 窗口的句炳


