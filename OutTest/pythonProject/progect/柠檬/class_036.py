"""
功能测试：
1写测试用例 TestCase
2执行测试用例 1：TestSuite储蓄用例 2：TestLoader找用例，加载用例 储存到1的testSuite
3对比实际结果 期望结果 判定用例是否通过 Assert
4出具报告 TextTestRunner

"""
import unittest
from progect.柠檬.math_method import MathMethod

class TestMathMethod(unittest.TestCase):

    def test_add_two_positive(self):#正数相加
        r=MathMethod(1,1).add()
        print("1+1结果集:",r)
        try:
            self.assertEqual(2, r)
        except AssertionError as e:
            print("出错了，断言错误是:{0}".format(e))
            raise e

    def test_add_two_zero(self):#0和正数相加
        r=MathMethod(0,1).add()
        print("0+1结果集:",r)
        try:
            self.assertEqual(0, r)
        except AssertionError as e:
            print("出错了，断言错误是:{0}".format(e))
            raise e

    def test_add_two_negative(self):#负数相加
        r=MathMethod(-1,-2).add()
        print("-1+-2结果集:",r)
        try:
            self.assertEqual(-3, r)
        except AssertionError as e:
            print("出错了，断言错误是:{0}".format(e))
            raise e


class TestMulti(unittest.TestCase):

    def test_multi_two_positive(self):#正数相乘
        r=MathMethod(1,1).multi()
        print("1*1结果集:",r)


    def test_multi_two_zero(self):#0和正数相乘
        r=MathMethod(0,1).multi()
        print("0*1结果集:",r)

    def test_multi_two_negative(self):#负数相乘
        r=MathMethod(-1,-2).multi()
        print("-1*-2结果集:",r)


if __name__ == '__main__':
    unittest.main #执行当前模块所有用例

