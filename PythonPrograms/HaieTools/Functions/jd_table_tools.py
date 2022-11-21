
import pandas as pd
import numpy as np
import time


class TableTools(object):

    def __init__(self):
        pass

    # 读取数据表
    def load_table(self,filepath,sheet_name="分仓"):
        return  pd.read_excel(filepath,sheet_name)


    # 查询京东库存
    def query_jd_stock(self,sku,):
        pass

    # 分仓库拆分总部库存表
    def split_stock_table(self,dataframe):
        data = dataframe[dataframe["京东仓"] == "顺义"]
        print(data)



if __name__ == '__main__':
    t = TableTools()
    table = t.load_table(r"D:\360MoveData\Users\Administrator\Desktop\jd_stock.xlsx")
    table = t.split_stock_table(table)
