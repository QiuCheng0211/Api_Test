
import re

# s = '{"memberId": "${memberID}", "pwd": "${pwd}"}'
#
# res=re.search('\$\{(.*?)\}',s)
# print(res)
# key=res.group(0)
# value = res.group(1)
# new_s=s.replace(key,"222")
# print(key,value)
# print(new_s)
"""正则表达式"""
class DoRegx:

    @staticmethod
    def do_regx(s):
        while re.search('\$\{(.*?)\}',s):
            key=re.search('\$\{(.*?)\}',s).group(0)
            value = re.search('\$\{(.*?)\}', s).group(1)
            s=s.replace(key,"222")
        return s

if __name__ == '__main__':
    s = '{"memberId": "${memberID}", "pwd": "${pwd}"}'
    print(DoRegx().do_regx(s))















