import pandas as pd
from Base import Base

class PriceRange(object):

    # 初始化
    def __init__(self):
        pass
    def getPriceRange(self, number, mode="1"):
        """
        通过单价计算属于哪个价位段；
        :param number: int 待判断数字
        :param mode: str 价位段模式（1,中怡康价位段、500,500一个价位段、1000,1000一个价位段 ）
        :return: str 价位段名称
                1  被判断的数字错误
                2  判断模式错误
        """
        num = None
        modeStr = None

        if Base.is_number(number):
            num = number
        else:
            return "1"
        modeStr = str(mode).strip()
        if modeStr == "1":
            pass
        elif modeStr == "500":
            pass
        elif modeStr == "1000":
            pass
        else:
            return "2"
    def getPerPrice(self,account,num):
        """
        计算单价
        :param account: 金额
        :param num: 数量
        :return:
        """
        if Base.is_number(account):
            if Base.is_number(num):
                pass
            else:
                return "2"
        else:
            return "1"


