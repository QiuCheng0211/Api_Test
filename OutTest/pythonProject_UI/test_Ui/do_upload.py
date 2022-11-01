import win32gui
import win32con

"""
使用案例1:打开百度云盘，点击“上传”弹出，打开选择文件的win窗口  即可启动程序
"""


def upload_file(filepath):
    # 一级窗口
    dialog = win32gui.FindWindow('#32770', '打开')
    # 二级窗口
    comboxex32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    # 三级窗口
    combox = win32gui.FindWindowEx(comboxex32, 0, 'ComboBox', None)
    # 文本的输入窗口-四级
    edit = win32gui.FindWindowEx(combox, 0, 'Edit', None)
    # 打开按钮一 二级窗口
    button = win32gui.FindWindowEx(dialog, 0, 'Button', '打开(&0)')

    # 输入地址
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)
    # 点击 打开按钮    提交文件夹
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)


upload_file(r"D:\自动化资料\python全栈自动化测试工程师第11期【柠檬班VIP】\1、开学典礼\x1429invz4w.p701.1")
