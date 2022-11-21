import openpyxl
import pandas as pd
import numpy as np
import requests
from openpyxl import Workbook
from openpyxl.utils import FORMULAE

1

class JD_Functions(object):

    def __init__(self):
        self.data = None

    def load_to_dataframe(self,filepath,sheet_name=None):
        self.data = pd.read_excel(filepath,sheet_name)

    def load_to_workbook(self,filepath,sheet_name=None):
        return openpyxl.load_workbook(filepath,sheet_name)

    def get_stockNum_from_dataframe(self,sku,storage_space):
        data = self.data[self.data["京东仓"] == storage_space]
        result = data[data["SKU"] == sku]["可用库存"]
        print(result)

    def get_price_from_jd(self,sku_id):
        user_agent = UserAgent.chrome_ua
        url = "https://item.m.jd.com/product/"+ str(sku_id) + ".html"
        responese = requests.get(url,user_agent)
        print(responese.text)

if __name__ == '__main__':
    jd = JD_Functions()
    price = jd.get_price_from_jd("100012809020")
    print(price)
