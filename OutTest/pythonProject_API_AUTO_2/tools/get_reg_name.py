import random

"""文件自动命名规则"""


class GetRegname:

    @staticmethod
    def get_reg_name():
        # 前缀
        name_prefix = "lemon_"
        # 中缀
        name_stem = "".join(random.sample('abcdefghijklmnopqrstuvwxyz', 5))
        # 后缀
        name_suffix = random.randint(10000, 99999)
        return name_prefix + name_stem + '_' + str(name_suffix)


if __name__ == '__main__':
    print(GetRegname.get_reg_name())
