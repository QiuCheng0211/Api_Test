import configparser

""""
输入：配置文件路径，段落名称(MODE)，选项名称(mode)
输出:字典形式返回选项的信息。例如：{"register":"all",
                            "login":[1,2,3,4],
                            "recharge":[1,2,3,4,5]}
"""


class ReadConfig:

    @staticmethod
    def get_config(filr_path, section, option):
        cf = configparser.ConfigParser()
        cf.read(filr_path)
        return cf[section][option]


"""以下是针对本py文件的调试"""
if __name__ == '__main__':
    from tools import project_path

    print(ReadConfig.get_config(project_path.case_config_path, "MODE", "mode"))
