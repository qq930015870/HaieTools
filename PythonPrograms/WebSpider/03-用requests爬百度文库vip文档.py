
import requests
import re
import json
import os

class BaiduWK(object):

    def __init__(self):
        self.path = None
        self.session = requests.session()
        self.target_url = None

    # 保存路径是否存在，不存在则创建
    def path_is_existed(self,path):
        if not os.path.exists(path):
            os.mkdir(path)

    # 判断目标文件类型
    def target_type(self):
        pass

    # 解析文档id
    # https://wenku.baidu.com/view/00d4dc2dd6d8d15abe23482fb4daa58da1111cd2.html?fr=income5-doc-search&_wkts_=1669368560908&wkQuery=%E5%A4%8D%E7%9B%98PPT
    # https://wkretype.bdimg.com/retype/zoom/d538122a55270722192ef77e?pn=1&o=jpg_6&md5sum=e1ad70f71ade153cca60f5aa8583a532&sign=b9e3b5d804&png=0-4576&jpg=0-87093
    # https://wkretype.bdimg.com/retype/zoom/d538122a55270722192ef77e?pn=2&o=jpg_6&md5sum=e1ad70f71ade153cca60f5aa8583a532&sign=b9e3b5d804&png=4577-9153&jpg=87094-194717

    def parser_doc_id(self,url):
        return re.findall("https://wenku.baidu.com/view/(.*?)\?",url)[0]

    def parser_doc_md5sum(self,url):
        pass

    def parser_doc_info(self,url):
        return self.session.get(url).content



    # 主函数
    def main(self):
        pass

if __name__ == '__main__':

    c= BaiduWK()
    # doc = c.parser_doc_id("https://wenku.baidu.com/view/2039a0feacaad1f34693daef5ef7ba0d4a736daa?aggId=00d4dc2dd6d8d15abe23482fb4daa58da1111cd2&fr=catalogMain&_wkts_=1669372272473&wkQuery=%E5%A4%8D%E7%9B%98PPT")
    # print(doc)
    c.parser_doc_info("https://wenku.baidu.com/view/2039a0feacaad1f34693daef5ef7ba0d4a736daa?aggId=00d4dc2dd6d8d15abe23482fb4daa58da1111cd2&fr=catalogMain&_wkts_=1669372887916")