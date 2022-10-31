import configparser



class ReadConfig:
    def read_config(self,file_name,section,option):
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding="utf-8")
        # print(cf.sections())
        # print(cf.items(section))
        return cf.get(section,option)

if __name__ == '__main__':
    res=ReadConfig().read_config("case.config","MODE","mode")
    print(res)



