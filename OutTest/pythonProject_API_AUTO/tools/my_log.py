import logging


class MyLog:

    def my_log(self,msg,level):

        #创建一个日志收集器
        my_logger=logging.getLogger("收集器")

        #设定收集器级别
        my_logger.setLevel("DEBUG")
        #设置输出格式
        formatter=logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s")#时间 等级 文件名 收集器 日志信息

        #创建一个我们自己的输出渠道
        ch=logging.StreamHandler()
        ch.setLevel("DEBUG")
        ch.setFormatter(formatter)

        fh=logging.FileHandler("py11.txt",encoding="utf-8")
        fh.setLevel("DEBUG")
        fh.setFormatter(formatter)

        #两者对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        #收集日志
        if level=="DEBUG":
            my_logger.debug(msg)
        elif level=="INFO":
            my_logger.info(msg)
        elif level == "WARNING":
            my_logger.warning(msg)
        elif level == "ERROR":
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        #关闭收集器
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.my_log(msg,"DEBUG")

    def info(self,msg):
        self.my_log(msg,"INFO")

    def warning(self,msg):
        self.my_log(msg,"WARNING")

    def error(self,msg):
        self.my_log(msg,"ERROR")

    def critical(self,msg):
        self.my_log(msg,"CRITICAL")

# if __name__ == '__main__':
#     MyLog().debug("一级")

    # MyLog().my_log("一级","DEBUG")
    # MyLog().my_log("二级", "INFO")
    # MyLog().my_log("三级", "WARNING")
    # MyLog().my_log("四级", "ERROR")
    # MyLog().my_log("五级", "CRITICAL")