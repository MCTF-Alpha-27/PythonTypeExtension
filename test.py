"""
type.py的功能测试
"""
from type import *

class String测试:
    @staticmethod
    def 基本测试():
        test = String("Hello World")
        a = String("a")
        b = String("b")
        c = "c"
        d = a + b + c
        print(test)
        print(a + b)
        print(d, type(d))

    @staticmethod
    def 运算符判断():
        a = String("1")
        b = String("1")
        c = String("2")
        print(a == b, a == c, b == c)
        print(a > b, a < b, a > c, a < c, b > c, b < c)
        print(a != b, a != c, b != c)

    @staticmethod
    def 方法测试():
        a = String("114514")
        print(a.isNumber(), a.isEven(), a.isOdd())
        print(a.hasSpace())
        b = a.replace("114", "")
        print(b, type(b))
        print(a.subString(0), a.subString(0, 3))
        print(a.toList())

class Integer测试:
    @staticmethod
    def 基本测试():
        a = Integer(1)
        b = Integer(1)
        print(a + b)
        c = 1
        print(a + c, b + c)
        d = a + b + c
        print(d, type(d))

    @staticmethod
    def 运算符判断():
        a = Integer(1)
        b = Integer(1)
        c = Integer(2)
        print(a == b, a == c, b == c)
        print(a > b, a < b, a > c, a < c, b > c, b < c)
        print(a != b, a != c, b != c)

    @staticmethod
    def 方法测试():
        a = Integer(114514)
        print(a.isEven(), a.isOdd())
        b = a.replace("114", "")
        print(b, type(b))

if __name__ == "__main__":
    String测试.基本测试()
    String测试.运算符判断()
    String测试.方法测试()

    Integer测试.基本测试()
    Integer测试.运算符判断()
    Integer测试.方法测试()