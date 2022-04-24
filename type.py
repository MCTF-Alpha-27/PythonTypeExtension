__author__ = "Jerry"
__version__ = "1.2.3"

class NotComposedOfNumbersError(Exception):
    "不是由数字组成的字符串使用String对象的toInt()函数或toInteger()函数时抛出"
    pass

class String:
    "字符串类，是对Python原版字符串的加强"
    def __init__(self, str_) -> None:
        if type(str_) is not str:
            raise TypeError(
                "请使用字符串类型来创建String对象"
            )
        self.__str = str_
        self.length = len(str_) # 字符串大小

    def __repr__(self) -> str:
        return self.__str

    __str__ = __repr__

    def __len__(self):
        "使用len()函数时调用"
        return self.length

    def __add__(self, other):
        "当与一个字符串或另一个String对象进行加操作时调用"
        if type(other) is String:
            return String(self.__str + other.__str)
        else:
            return String(self.__str + other)

    def __sub__(self, other):
        "当与一个字符串或另一个String对象进行减操作时调用"
        if type(other) is String:
            return String(self.__str - other.__str)
        else:
            return String(self.__str - other)

    def __eq__(self, other) -> bool:
        "等于判断"
        if type(other) is String:
            return self.__str == other.__str
        else:
            return self.__str == other

    def __ne__(self, other) -> bool:
        "不等于判断"
        if type(other) is String:
            return self.__str != other.__str
        else:
            return self.__str != other

    def __lt__(self, other) -> bool:
        "小于判断"
        if type(other) is String:
            return self.__str < other.__str
        else:
            return self.__str < other

    def __gt__(self, other) -> bool:
        "大于判断"
        if type(other) is String:
            return self.__str > other.__str
        else:
            return self.__str > other

    def __le__(self, other) -> bool:
        "小于等于判断"
        if type(other) is String:
            return self.__str <= other.__str
        else:
            return self.__str <= other

    def __ge__(self, other) -> bool:
        "大于等于判断"
        if type(other) is String:
            return self.__str >= other.__str
        else:
            return self.__str >= other

    def isNumber(self):
        "判断字符串是否由数字组成，返回布尔值"
        try:
            int(self.__str)
        except ValueError:
            return False
        else:
            return True

    def toInt(self):
        "如果能，将字符串转成整数，否则抛出NotComposedOfNumbersError异常"
        try:
            return int(self.__str)
        except ValueError as e:
            raise NotComposedOfNumbersError(
                "字符串不是由数字组成的"
            ) from e

    def toInteger(self):
        "如果能，将字符串转成Integer对象，否则抛出NotComposedOfNumbersError异常"
        try:
            return Integer(int(self.__str))
        except ValueError as e:
            raise NotComposedOfNumbersError(
                "字符串不是由数字组成的"
            ) from e

class Integer:
    "整数类型，是对Python原版整数的加强"
    def __init__(self, int_) -> None:
        if type(int_) is not int:
            raise TypeError(
                "请使用整数类型创建Integer对象"
            )
        self.__int = int_

    def __repr__(self) -> str:
        return str(self.__int)

    __str__ = __repr__

    def __add__(self, other):
        "当与一个整数或另一个Integer对象进行加操作时调用"
        if type(other) is Integer:
            return Integer(self.__int + other.__int)
        else:
            return Integer(self.__int + other)

    def __sub__(self, other):
        "当与一个整数或另一个Integer对象进行减操作时调用"
        if type(other) is Integer:
            return Integer(self.__int - other.__int)
        else:
            return Integer(self.__int - other)

    def __eq__(self, other) -> bool:
        "等于判断"
        if type(other) is Integer:
            return self.__int == other.__int
        else:
            return self.__int == other

    def __ne__(self, other) -> bool:
        "不等于判断"
        if type(other) is Integer:
            return self.__int != other.__int
        else:
            return self.__int != other

    def __lt__(self, other) -> bool:
        "小于判断"
        if type(other) is Integer:
            return self.__int < other.__int
        else:
            return self.__int < other

    def __gt__(self, other) -> bool:
        "大于判断"
        if type(other) is Integer:
            return self.__int > other.__int
        else:
            return self.__int > other

    def __le__(self, other) -> bool:
        "小于等于判断"
        if type(other) is Integer:
            return self.__int <= other.__int
        else:
            return self.__int <= other

    def __ge__(self, other) -> bool:
        "大于等于判断"
        if type(other) is Integer:
            return self.__int >= other.__int
        else:
            return self.__int >= other

    def toStr(self):
        "将整数转成字符串"
        return str(self.__int)

    def toString(self):
        "将整数转成String对象"
        return String(str(self.__int))