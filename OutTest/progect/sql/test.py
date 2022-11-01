from selenium import webdriver
driver_path=r"D:\python3.7\chromedriver.exe" #
driver=webdriver.Chrome (executable_path=driver_path)
driver.get("https://www.baidu.com")
print (driver.page_source)