import unittest
from ddt import ddt,data,unpack


test_data=[{"no":1,"name":"黄子怡"},{"no":2,"name":"小瓶子"}]
# test_data=[{1,2},{3,4}]
# test_data=[1,3]

@ddt
class TestMath(unittest.TestCase):


    @data(*test_data)
    @unpack
    def test_print_data(self,no,name):
        print("no",no)
        print("name", name)

# if __name__ == '__main__':
#     TestMath().test_print_data