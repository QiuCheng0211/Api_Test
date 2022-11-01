import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

# QQ邮件发送的用户名和密码，常识：第三方授权码
# use = "2438545146@qq.com"
# pwd = "hjjmnilpepeldhgb" #授权码

# 163邮件发送的用户名和密码，常识：第三方授权码
use = "17701583363@163.com"
pwd = "ASSIHTGAYYOHBPYX"  # 授权码

now = time.strftime("%Y/%m/%d %H:%M:%S")  # 获取时间戳

"""输入email_to收件人邮箱   email_cc抄送人和filepath附件路径属于非必传  """

class sendEmail:
    def send_email(self, email_to,email_cc=None, filepath=None):
        msg = MIMEMultipart()  # 创建模拟对象
        msg["Subject"] = now + "测试报告"  # 邮件主题
        msg["From"] = use  # 发件人
        msg["To"] = email_to  # 收件人
        msg["Cc"] = email_cc  # 抄送

        # 这是文字部分
        part = MIMEText("这是自动化结果请查收")  # 邮件正文
        msg.attach(part)

        # 这是发送一个附件
        if filepath is None:
            print("没有附件")
        else:
            for root, dirs, files in os.walk(filepath):
                for dir in dirs:
                    print(os.path.join(root, dir))
                for file in files:
                    i = os.path.join(root, file)
                    part = MIMEApplication(open(i, 'rb').read())
                    part.add_header("Content-Disposition", "attachment", filepath=i)
                    msg.attach(part)
        # s=smtplib.SMTP_SSL("smtp.qq.com", timeout=465)#连接QQ邮箱 stp邮件服务器，端口默认是25  465  587
        s = smtplib.SMTP_SSL("smtp.163.com", timeout=465)  # 连接163邮箱  stp邮件服务器，端口默认是25  465  587
        s.login(use, pwd)  # 登陆服务器
        s.sendmail(use, email_to, msg.as_string())  # 发送邮件
        s.close()


if __name__ == '__main__':
    sendEmail().send_email("2438545146@qq.com",filepath="../test_resuit/html_report/")
