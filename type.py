"""
对Python原版类型的扩展
"""
__author__ = "Jerry"
__version__ = "1.3.4"

__all__ = ["String", "Integer", "List"]

class NotComposedOfNumbersError(Exception):
    "不是由数字组成的字符串使用某些方法时抛出"
    pass

class String(str):
    "字符串类，是对Python原版字符串的扩展"
    def __init__(self, str_) -> None:
        if type(str_) is not str:
            raise TypeError(
                "请使用字符串类型来创建String对象"
            )
        self.__str = str_
        self.length = len(str_) # 字符串大小

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

    def getNormal(self):
        "将扩展类型转为原版类型"
        return self.__str

    def isEven(self):
        "判断数字是否是偶数，返回布尔值（前提是这个字符串是由数字组成的，否则抛出NotComposedOfNumbersError异常）"
        if self.toInt() % 2 == 0:
            return True
        else:
            return False

    def isOdd(self):
        "判断数字是否是奇数，返回布尔值（前提是这个字符串是由数字组成的，否则会出NotComposedOfNumbersError异常）"
        if self.toInt() % 2 == 0:
            return False
        else:
            return True

    def hasSpace(self):
        "判断字符串中是否存在空格，返回布尔值"
        for i in self.__str:
            if i == " ":
                return True
        return False

    def replace(self, /, past, now):
        "在前一个括号内填写字符串内要匹配的元素，后一个括号内填入要被替换成的元素，这样所有匹配的元素都会被替换为要被替换成的元素，最后返回String对象"
        return String(self.__str.replace(past, now))

    def subString(self, /, range1, range2=None):
        "字符串切片。在前一个括号中填入起始索引值，后一个括号中填入结束索引值，将会返回一个String对象。若索引值超出了字符串范围，将会返回空字符串。"
        if range2 is None:
            range2 = range1 + 1
        return String(self.__str[range1:range2])

    def toList(self):
        "将字符串转换为列表"
        return list(self.__str)

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

class Integer(int):
    "整数类型，是对Python原版整数的扩展"
    def __init__(self, int_) -> None:
        if type(int_) is not int:
            raise TypeError(
                "请使用整数类型创建Integer对象"
            )
        self.__int = int_

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

    def getNormal(self):
        "将扩展类型转为原版类型"
        return self.__int

    def isEven(self):
        "判断数字是否是偶数，返回布尔值"
        if self.__int % 2 == 0:
            return True
        else:
            return False
    
    def isOdd(self):
        "判断数字是否是奇数，返回布尔值"
        if self.__int % 2 == 0:
            return False
        else:
            return True

    def isDivisible(self, number):
        "判断数字是否能被某个数整除，返回布尔值"
        if type(number) is Integer:
            return self.__int % number.__int == 0
        else:
            return self.__int % number == 0

    def replace(self, /, past, now):
        "在前一个括号内填写字符串内要匹配的元素，后一个括号内填入要被替换成的元素，这样所有匹配的元素都会被替换为要被替换成的元素，最后返回Integer对象"
        return Integer(int(self.toStr().replace(past, now)))

    def toStr(self):
        "将整数转成字符串"
        return str(self.__int)

    def toString(self):
        "将整数转成String对象"
        return String(str(self.__int))

class List(list):
    "列表类型，是对Python原版列表的扩展"
    def __init__(self, list_) -> None:
        if type(list_) is not list:
            raise TypeError(
                "请使用列表类型创建List对象"
            )
        self.__list = list_
        self.length = len(list_) # 列表长度

    def __repr__(self) -> str:
        r = []
        for i in self.__list:
            if type(i) is str:
                r.append("'%s'"%i)
            elif type(i) is int:
                r.append(str(i))
            elif type(i) is String:
                r.append("<Extension Type String '%s'>"%i.getNormal())
            elif type(i) is Integer:
                r.append("<Extension Type Integer %s>"%i.toStr())
            elif type(i) is List:
                r.append("<Extension Type List %s>"%i.getNormal())
        return "[%s]"%(", ".join(r))

    __str__ = __repr__

    def __len__(self):
        "使用len()函数时调用"
        return self.length

    def __add__(self, other):
        "当与一个整数或另一个List对象进行加操作时调用"
        if type(other) is List:
            return List(self.__list + other.__list)
        else:
            return List(self.__list + other)

    def __sub__(self, other):
        "当与一个整数或另一个List对象进行减操作时调用"
        if type(other) is List:
            return List(self.__list - other.__list)
        else:
            return List(self.__list - other)

    def __eq__(self, other) -> bool:
        "等于判断"
        if type(other) is List:
            return self.__list == other.__list
        else:
            return self.__list == other

    def __ne__(self, other) -> bool:
        "不等于判断"
        if type(other) is List:
            return self.__list != other.__list
        else:
            return self.__list != other

    def __lt__(self, other) -> bool:
        "小于判断"
        if type(other) is List:
            return self.__list < other.__list
        else:
            return self.__list < other

    def __gt__(self, other) -> bool:
        "大于判断"
        if type(other) is List:
            return self.__list > other.__list
        else:
            return self.__list > other

    def __le__(self, other) -> bool:
        "小于等于判断"
        if type(other) is List:
            return self.__list <= other.__list
        else:
            return self.__list <= other

    def __ge__(self, other) -> bool:
        "大于等于判断"
        if type(other) is List:
            return self.__list >= other.__list
        else:
            return self.__list >= other

    def getNormal(self):
        "将扩展类型转为原版类型"
        return self.__list

    def toStrList(self):
        "如果列表包含整数，返回一个将整数转为字符串的列表"
        strList = []
        for i in self.__list:
            if type(i) is int:
                strList.append(str(i))
            else:
                strList.append(i)
        return strList

    def toIntList(self):
        "如果列表包含字符串，返回一个将字符串转为整数的列表"
        intList = []
        for i in self.__list:
            if type(i) is str:
                if i.isdigit():
                    intList.append(int(i))
            else:
                intList.append(i)
        return intList

    def toStringList(self):
        "如果列表包含字符串，返回一个将字符串转为String对象的列表"
        stringList = []
        for i in self.__list:
            if type(i) is str:
                stringList.append(String(i))
            else:
                stringList.append(i)
        return List(stringList)

    def toIntegerList(self):
        "如果列表包含整数，返回一个将整数转为Integer对象的列表"
        integerList = []
        for i in self.__list:
            if type(i) is int:
                integerList.append(Integer(i))
            else:
                integerList.append(i)
        return List(integerList)
