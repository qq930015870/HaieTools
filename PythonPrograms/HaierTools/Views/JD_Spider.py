
from selenium import webdriver


class JD_Spider(object):

    def __init__(self):
        pass

    def getRequest(self):
        rs = requests.get("https://item.m.jd.com/product/100039851902.html").text
        print(rs)
        pattern = ""

if __name__ == '__main__':
    j = JD_Spider()
    j.getRequest()