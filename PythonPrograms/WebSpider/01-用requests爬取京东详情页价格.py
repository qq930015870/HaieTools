import requests
import threading
import time
from bs4 import BeautifulSoup

"""
    ★ 前期准备：
    1、产品详情页的链接是：https://item.m.jd.com/product/100008282285.html
    2、京东手机端仅通过user-agent参数反爬，取数相对简单一些
    
    ★ 思路总结（多线程版）：
    1、获取网页信息
    2、解析产品价格
    
"""


class QuerySalePrice(threading.Thread):

    # 存储每种浏览器所带的headers信息
    class BrowserHeadersContainer:
        iphone_headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        }  # iphone手机的headers
        chrome_headers = {

        }  # chrome的headers

    # 实例化一个参数存储器对象
    browser_headers = BrowserHeadersContainer()

    # 初始化
    def __init__(self, target_list,  headers="Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"):
        super(QuerySalePrice,self).__init__()
        self.headers = QuerySalePrice.browser_headers.iphone_headers  # 自定义的BrowserHeaders用来存储各种headers
        self.target_list = target_list

    # 从互联网获取网页源代码
    def get_page_source(self,sku_id):
        """
        获取详情页源代码
        :param sku_id: str
        :return: page_code str
        """
        url = "https://item.m.jd.com/product/" + str(sku_id) + ".html"
        page_code = requests.get(url, headers= self.headers).text
        return page_code

    # 用beautifulsoup解析网页
    def get_price(self, page_code: str) -> str:
        """
        从网页源代码中获取价格
        :type page_code: str
        :rtype: str
        :param page_code:
        """
        page_source = page_code
        soup = BeautifulSoup(page_source, 'html.parser')
        price = soup.find("span", id="priceSale").em.text.strip()
        if price:
            return price
        else:
            return "未取到价格"

    # 线程类run方法
    def run(self):
        if len(self.target_list) != 0:
            for item in self.target_list:
                code = self.get_page_source(item)
                price = self.get_price(code)
                print(item,price)
                time.sleep(1)
        else:
            raise ValueError("目标列表为空，无法查询")



if __name__ == '__main__':
    t1 = QuerySalePrice(["100008102195","100020997746","100013309162"])
    t2 = QuerySalePrice(["100008282285","100015323308"])
    t1.start()
    t2.start()
    # print(t1)