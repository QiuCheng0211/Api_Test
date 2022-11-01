import logging
import time
from common import dir_config

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime


# 封装基本函数 执行日志 异常处理 失败截图
# 所有页面的公共部分

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, locator, wait_time=30, poll_frequency=0.5, doc=""):
        logging.info("等待元素{0}可见".format(locator))
        # 如果存在就返回Ture，如果不存在，就返回False
        try:
            # 开始等待的时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait_time, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待的时间
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            # 求一个差值，写在日志当中，等待多久
            logging.info("{0}：元素{1}已可见，等待起始时间：{2}，等待时间结束:{3}等待时长：{4}".format(doc, locator, start, end, wait_times))
        except:
            logging.exception("等待元素可见异常！！！")
            # 截图操作
            self.save_screenshots(doc)
            raise

    # 等待元素存在
    def wait_element(self):
        pass

    # 查找元素
    def get_element(self, locator, doc=""):
        logging.info("查找元素:{}".format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败！！！")
            # 截图操作
            self.save_screenshots(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        # 元素操作
        logging.info("{0}点击元素：{1}".format(doc, locator))
        try:
            ele.click()
        except:
            logging.exception("元素点击失败！！！")
            # 截图操作
            self.save_screenshots(doc)
            raise

    # 输入操作
    def input_text(self, locator, text, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        # 输入操作
        try:
            ele.send_keys(text)
        except:
            logging.exception("元素输入失败！！！")
            # 截图操作
            self.save_screenshots(doc)
            raise

    # 获取元素的文本内容
    def get_text(self, locator, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        try:
            return ele.text
        except:
            logging.exception("获取元素文本内容！！！")
            # 截图操作
            self.save_screenshots(doc)
            raise

    # 获取元素的属性
    def get_element_attribute(self, locator, attr, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        try:
            return ele.get_attribute(attr)
        except:
            logging.exception("获取元素属性失败！！！")
            # 截图操作
            self.save_screenshots(doc)
            raise

    # alert处理
    def alert_action(self, action="accept"):
        pass

    # iframe切换
    def switch_iframe(self, iframe_reference):
        pass

    # 上传操作
    def upload_file(self):
        pass

    # 滚动条处理
    # 窗口切换

    def save_screenshots(self, doc):
        # 图片名称:模块名_页面名称_操作名称_年月日_时分秒.png
        # file_name= "{0}_{1}.png".format(name,time.thread_time())
        # self.driver.save_screenshot("../Outputs/screenshots"+file_name)
        # logging.info("截取网页成功，文件路径为:{}".format(file_name))
        filePath = dir_config.screenshot_dir + \
                   "/{0}_{1}.png".format(doc, time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        try:
            self.driver.save_screenshot(filePath)
            logging.info("截取网页成功，文件路径为:{}".format(filePath))
        except:
            logging.exception("截图失败")