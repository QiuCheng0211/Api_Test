import logging

"""
独立的日志文件 输入需要打印的信息即可  例如MyLog().debug("一级")
设置了两个输出  一个是输出到控制台  一个是输出到指定文件夹
"""


class MyLog:

    def my_log(self, msg, level):

        # 创建一个日志收集器  以及设置收集器的名字
        my_logger = logging.getLogger("两个流氓一个好市民")

        # 设定收集器级别
        my_logger.setLevel("DEBUG")
        # 设置输出格式
        formatter = logging.Formatter(
            "%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s")  # 时间 等级 文件名 收集器名字 日志信息

        # 创建一个输出到打印台的输出渠道
        ch = logging.StreamHandler()  # 输出到控制台
        ch.setLevel("DEBUG")  # 设置输出控制台日志级别
        ch.setFormatter(formatter)  # 指定设置输出格式

        # 创建第二个输出渠道打印到指定的文本文件
        fh = logging.FileHandler("test_resuit/logs/py01.txt", encoding="utf-8")  # 输出文本文件
        fh.setLevel("DEBUG")  # 设置输出到文本文件的日志级别
        fh.setFormatter(formatter)  # 指定设置输出格式

        # 两者对接
        my_logger.addHandler(ch)  # 收集器与创建的第一个输出渠道对接
        my_logger.addHandler(fh)  # 收集器与创建的第二个输出渠道对接

        # 收集日志
        if level == "DEBUG":
            my_logger.debug(msg)
        elif level == "INFO":
            my_logger.info(msg)
        elif level == "WARNING":
            my_logger.warning(msg)
        elif level == "ERROR":
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        # 关闭收集器
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, "DEBUG")

    def info(self, msg):
        self.my_log(msg, "INFO")

    def warning(self, msg):
        self.my_log(msg, "WARNING")

    def error(self, msg):
        self.my_log(msg, "ERROR")

    def critical(self, msg):
        self.my_log(msg, "CRITICAL")
