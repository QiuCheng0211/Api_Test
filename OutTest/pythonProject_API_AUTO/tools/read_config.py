import configparser

class ReadConfig:

    @staticmethod
    def get_config(filr_path,section,option):
        cf=configparser.ConfigParser()
        cf.read(filr_path)
        return cf[section][option]

if __name__ == '__main__':
    from tools import project_path
    print(ReadConfig.get_config(project_path.case_config_path,"MODE","mode"))
