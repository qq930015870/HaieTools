class Headers:
    headers="123"

class GetVideoSpider(object):
    """
    获取网页视频的爬虫类
    """
    def __init__(self):
        """
        初始化视频爬虫
        """
        self.headers = Headers.headers
        self.target_addr = ""
