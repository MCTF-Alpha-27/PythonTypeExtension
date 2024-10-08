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
        print(a.isEven(), a.isOdd())
        print(a.hasSpace())
        b = a.replace("114", "")
        print(b, type(b))
        print(a[0], a[0:3], type(a[0]))
        print(a.toList())
        print(a.getNormal())

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
        print(a.isDivisible(114514), a.isDivisible(b))
        print(a.getNormal())

class List测试:
    @staticmethod
    def 基本测试():
        a = List(["a", "b", "c"])
        b = ["a", "b"]
        c = List(["1", "2", "3"])
        print(a, b, c)
        print(a + b, a + c, c + b)

    @staticmethod
    def 运算符测试():
        a = List([1, 2, 3])
        b = List([4, 5, 6])
        c = List([1, 2, 3])
        print(a == b, a == c, b == c)
        print(a > b, a < b, a > c, a < c, b > c, b < c)
        print(a != b, a != c, b != c)

    @staticmethod
    def 方法测试():
        a = List(["1", "2", "3"])
        b = List([1, 2, 3])
        c = List([1, "2", "3", 4])
        d = List(["a", List(["b"])])
        print(a, a.length)
        print(a.toIntList())
        print(a.getNormal())
        print(b, b.length)
        print(b.toStrList())
        print(a.getNormal())
        print(c, c.length)
        print(c.toIntList(), c.toStrList())
        print(c.toIntegerList(), c.toStringList())
        print(d, d.length)

if __name__ == "__main__":
    String测试.基本测试()
    String测试.运算符判断()
    String测试.方法测试()

    Integer测试.基本测试()
    Integer测试.运算符判断()
    Integer测试.方法测试()

    List测试.基本测试()
    List测试.运算符测试()
    List测试.方法测试()
