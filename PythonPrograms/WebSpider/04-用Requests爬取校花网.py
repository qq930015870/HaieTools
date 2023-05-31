
"""
目标：爬取校花网图片
入口URL:https://www.ruyile.com/nice/?s=1&p=1
网站分析：
1、s是地区代码，从左到右，p是页码
2、需求数据全部都在网页源代码中
3、网站无任何反爬策略

开发环境：Pycharm2021.3
运行环境：Anaconda3
"""

import requests
import re
from bs4 import BeautifulSoup

class XHSpider:

    def __init__(self):
        pass

    def load_url(self,url):
        return requests.get(url).text

    def parser_item_url(self,html):
        soup = BeautifulSoup(html,"html.parser")
        divs = soup.find_all("div",{"class":"m3_xhtp sdtk"})


        print(divs)
        # for div in divs:


    def main(self):
        html = self.load_url("https://www.ruyile.com/nice/?s=1")
        self.parser_item_url(html)

if __name__ == '__main__':
    x = XHSpider()
    x.main()
